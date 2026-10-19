# Mini Sprint Plan: Story 2.1 — Score Leads with BANT

> **Learner:** Jezreal Momoh  
> **Track:** DTA Agentic AI in Software Development — Week 2 Takeaway Deliverable  
> **Linked Requirements:** `FR-06` (Score leads using BANT) · `NFR-04` (Consistent BANT accuracy on test set) · `NFR-01` (Latency < 5 s)  

---

**Epic:** `E2` (Lead Qualification and Negotiation)   **Story points:** `5 pts`  
**Story:** As a **supplier**, I want leads scored on **Budget, Authority, Need, and Timeline (BANT)**, so that I focus my sales effort on serious buyers.  
**Sprint Goal (one sentence):** Enable the Seller Agent to automatically score and classify incoming buyer inquiries using the BANT framework without inventing missing qualification details.  

---

## Acceptance Criteria (`Given / When / Then`)

- **AC-1 (Complete BANT Scoring & Tiering):** **Given** a buyer inquiry containing clear signals for Budget, Authority, Need, and Timeline, **when** `score_lead_bant()` processes the lead, **then** the agent computes a total BANT score (`0–100`), assigns a priority tier (`Hot` $\ge 75$, `Warm` $40\text{–}74$, `Cold` $< 40$), and logs the breakdown for each of the four criteria.
- **AC-2 (No Invented Qualification Data):** **Given** a buyer inquiry that is missing 1 or more BANT fields (e.g., no budget or timeline mentioned), **when** the agent evaluates the lead, **then** it explicitly marks the missing dimensions as `"unknown"` ($0\text{ pts}$ for that dimension) and generates a targeted follow-up question rather than guessing or hallucinating buyer details.
- **AC-3 (High-Value / Enterprise Escalation Guardrail):** **Given** a buyer lead requesting a contract value above **\$50,000** (or **₦500,000**) or custom enterprise terms, **when** the agent processes the lead, **then** it flags the lead with `status = "needs_supplier_review"` so the supplier can engage personally.
- **AC-4 (Measurable — Accuracy & Zero Hallucination):** **Given** a benchmark dataset of **20 labeled buyer leads** (including complete, partial, and vague inquiries), **when** evaluated by the Seller Agent, **then** at least **90% (18 of 20)** match the ground-truth tier (`NFR-04`) and **0 of 20 cases** contain invented buyer attributes.
- **AC-5 (Measurable — Latency):** **Given** 20 benchmark test runs of the lead scoring workflow, **when** a buyer inquiry is submitted, **then** **95% (19 of 20)** of scoring responses complete in **under 5 seconds** (`NFR-01`).

---

## Tasks (with Coverage Test: Build + Proof)

| # | Task | Tag | Size | Depends on | Covers (`Build` vs. `Proof`) |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | Define the BANT scoring rubric (`25 pts` per dimension), tier thresholds (`Hot`/`Warm`/`Cold`), and JSON schema for `20` benchmark buyer leads | `DATA` | S (0.5d) | PO confirmation of rubric | **Build:** `AC-1`, `AC-4` |
| **2** | Implement `score_lead_bant(lead_payload)` to calculate dimension scores, total score (`0–100`), and tier classification with audit logging | `DEV` | M (1d) | Task 1 | **Build:** `AC-1` |
| **3** | Add missing-field detection in `score_lead_bant()` to mark absent BANT signals as `"unknown"` and return follow-up prompts instead of guessing | `DEV` | S (0.5d) | Task 2 | **Build:** `AC-2` |
| **4** | Implement high-value / custom-term guardrail check that sets `status = "needs_supplier_review"` when deal size exceeds threshold | `DEV` | S (0.5d) | Task 2 | **Build:** `AC-3` |
| **5** | Format the supplier-facing BANT scorecard summary (`score`, `tier`, `breakdown`, `missing_fields`, `review_flag`) for easy inspection | `UX` | S (0.5d) | Tasks 2, 3, 4 | **Build:** `AC-1`, `AC-3` |
| **6** | Write unit tests (`test_bant_scorer.py`) covering full leads, missing BANT fields, boundary scores (`39`, `40`, `74`, `75`), and high-value flagging | `QA` | M (1d) | Tasks 2, 3, 4 | **Proof:** `AC-1`, `AC-2`, `AC-3` |
| **7** | Run the 20-lead evaluation benchmark to measure tier accuracy ($\ge 90\%$), zero-hallucination rate (`20/20`), and $< 5\text{ s}$ latency (`95%`) | `EVAL` | S (0.5d) | Tasks 1, 6 | **Proof:** `AC-4`, `AC-5` |

> **Coverage Test Verification:**
> - `AC-1` is built by **Tasks 1, 2, 5** and proven by **Task 6**.
> - `AC-2` is built by **Task 3** and proven by **Task 6**.
> - `AC-3` is built by **Tasks 4, 5** and proven by **Task 6**.
> - `AC-4` & `AC-5` are built by **Tasks 1–4** and proven by **Task 7**.
> - **Result:** 100% of Acceptance Criteria have both a **build task** and a **proof task**.

---

## Dependencies and Blockers

| Dependency | What Could Block Us | How We Reduce It |
| :--- | :--- | :--- |
| **BANT Weighting Rules (`Decision`)** | Suppliers might disagree on whether Budget or Need carries more weight, stalling `Task 2`. | Agree on a default equal weighting (`25 pts` each for B, A, N, T) with the Product Owner during Sprint Planning and make weights configurable in a dictionary. |
| **Benchmark Lead Dataset (`Data`)** | Waiting for real historical eComMART buyer inquiries could block `Task 6` and `Task 7`. | Create a synthetic 20-lead JSON sample dataset (`leads_sample.json`) on Day 1 covering `Hot`, `Warm`, `Cold`, and incomplete cases. |
| **Product Catalog Pricing (`Task-to-Task`)** | Checking whether a buyer's budget matches product pricing depends on `ProductCatalog` from Story 1.1. | Pass `expected_order_value` or use the 3-SKU mock catalog stub so `score_lead_bant()` can be tested independently. |

---

## Risks

| Risk | Likelihood (L/M/H) | Impact (L/M/H) | Mitigation |
| :--- | :---: | :---: | :--- |
| **AI-Specific Risk — Hallucinated Qualification Signals:** The agent infers "Authority" or "Budget" from polite buyer phrasing when none was stated, inflating a `Cold` lead into a `Hot` lead. | **M** | **H** | Require an explicit evidence span/field for each BANT dimension; default any unverified dimension to `"unknown"` ($0\text{ pts}$) and enforce `0/20` invented attributes in `Task 7`. |
| **False Negative Filtering:** Overly strict BANT rules classify a legitimate bulk buyer as `Cold` because their initial message was brief (*"Need 500 units ASAP, send quote"*). | **M** | **M** | Route partial leads with strong `Need` + `Timeline` into `"Warm (Needs Clarification)"` and trigger automatic follow-up questions (`AC-2`) rather than rejecting them. |
| **PR Review Bottleneck:** All `DEV` tasks finish on Day 4 and pile up in `In Review`, violating the `WIP ≤ 2` limit and delaying `QA`/`EVAL`. | **M** | **M** | Keep branches small and enforce the squad's 24-hour PR review rule; developers swarm on `In Review` cards before pulling new work. |
| **PII / Sensitive Data Exposure in Logs:** Buyer contact details or private budget notes get committed to the repo in test logs. | **L** | **H** | Use anonymized buyer IDs (`BUYER-001`) in sample data and failure logs, and enforce `.gitignore` rules (`SEC`). |

---

## Expected Failure Cases (for the Failure Log)

| ID | Input | Expected Output | What Could Go Wrong (Failure Mode) |
| :---: | :--- | :--- | :--- |
| **FL-01** | *"Hi, I am the Procurement Director. We need 200 industrial pumps next week. What is your best price?"* *(Budget missing)* | `Authority: 25`, `Need: 25`, `Timeline: 25`, `Budget: "unknown" (0)` → Score `75` (`Hot` / prompt for budget) | Agent invents a budget based on catalog price and logs `Budget: 25` (`100/100`), violating `AC-2` and `AC-4`. |
| **FL-02** | *"Just browsing your catalog for a school project, no budget or timeline."* | Score `0` → Tier `Cold`, no supplier alert triggered | Agent misinterprets keywords and scores the lead as `Warm`, wasting supplier sales time. |
| **FL-03** | *"We want a \$120,000 annual supply contract with 90-day net credit terms."* | `status = "needs_supplier_review"` (`AC-3` guardrail triggered) | Agent scores the lead normally and attempts to auto-negotiate custom credit terms outside policy. |

---

## Human Validation (Human-in-the-Loop)

- **Before (Setting Rules & Thresholds):** The **Product Owner and Supplier** define the BANT scoring weights (`0–25` per dimension), tier cutoffs (`Hot` $\ge 75$, `Warm` $40\text{–}74$, `Cold` $< 40$), and the high-value escalation threshold (\$50,000 / ₦500,000).
- **During (Active Escalation Guardrail):** Whenever a lead exceeds the high-value threshold, requests non-standard credit/contract terms (`AC-3`), or produces conflicting signals, the Seller Agent pauses autonomous handling and flags the lead (`needs_supplier_review`) for a human supplier to take over.
- **After (Audit & Calibration):** The **Supplier and `EVAL` Engineer** review the logged BANT scorecards and rationale weekly (`NFR-06`). Any misclassified lead discovered by a supplier is added to the **Failure Case Log** and converted into a permanent regression test in `test_bant_scorer.py`.

---

## Definition of Done

- [x] **Code reviewed and merged:** Pull Request approved by at least one teammate using the 5-point Reviewer Checklist and merged into `main`.
- [x] **Tests written and passing:** All unit tests in `test_bant_scorer.py` (`QA`) pass locally and on `main`.
- [x] **Demoed to the Product Owner:** Working BANT lead scoring demonstrated at Sprint Review and accepted against `AC-1` through `AC-5`.
- [x] **Story-Specific DoD Item:** Benchmark evaluation (`EVAL`) confirms **$\ge 90\%$ tier accuracy (18/20)** and **0 hallucinated BANT attributes (20/20)** on the test dataset, with all failure cases logged.
