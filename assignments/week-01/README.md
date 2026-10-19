# Week 1 Takeaway Exercise: User Stories, INVEST/SMART & NFRs

> **Course:** Agentic AI in Software Development Academy — Week 1  
> **Learner:** Jezreal Momoh  
> **Reference Guide:** [Week 1 Agile Fundamentals](../../docs/week-01-agile-fundamentals/README.md)  

---

## Exercise Prompt (from Week 1 Slide 37)

- **Task:** Create **5 User Stories** with **Acceptance Criteria** for an AI-enabled business application.
- **Validation Requirements:**
  - Write each story in standard Agile format: `As a <persona>, I want <capability>, so that <business value>.`
  - Write testable **Acceptance Criteria** in `Given / When / Then` format.
  - Validate each story against **INVEST** (*Independent, Negotiable, Valuable, Estimable, Small, Testable*) and **SMART** (*Specific, Measurable, Achievable, Relevant, Time-bound*).
  - Include at least **1 Non-Functional Requirement (NFR)** with a measurable target.

---

## Completed Deliverable: eComMART Agentic Commerce Backlog

### Story 1 — Inventory Verification Before Quoting (`Epic E1` · 5 pts)
- **User Story:** As a **supplier**, I want the Seller Agent to check my live stock in the `ProductCatalog` before sending a quote, so that I never promise items I do not have.
- **Acceptance Criteria:**
  - **AC-1 (Functional):** **Given** an SKU exists in the `ProductCatalog` with `stock > 0`, **when** a quote is requested, **then** the agent returns the exact available quantity.
  - **AC-2 (Functional):** **Given** an SKU has `stock == 0` or is missing from the catalog, **when** a buyer requests it, **then** the agent reports the item as `"unavailable"` and never invents stock.
  - **AC-3 (NFR — Reliability & Latency):** **Given** 20 benchmark test runs, **when** `check_stock(sku)` is evaluated, **then** **0 of 20 cases** contain invented stock (`NFR-02`) and **95% of replies** complete in under **5 seconds** (`NFR-01`).
- **SMART / INVEST Check:** Independent of negotiation logic; small (single catalog lookup tool); measurable (`20/20` zero-hallucination target).

---

### Story 2 — Automated BANT Lead Qualification (`Epic E2` · 5 pts)
- **User Story:** As a **supplier**, I want incoming buyer leads scored on **Budget, Authority, Need, and Timeline (BANT)**, so that I focus my sales effort on serious buyers.
- **Acceptance Criteria:**
  - **AC-1 (Functional):** **Given** a buyer inquiry containing budget, decision role, quantity need, and purchase timeline, **when** the Seller Agent evaluates the lead, **then** it assigns a structured BANT score (`0–100`) and tier (`Hot`, `Warm`, `Cold`).
  - **AC-2 (Functional):** **Given** a buyer inquiry missing 2 or more BANT dimensions, **when** processed, **then** the agent marks the missing fields as `"unknown"` and prompts for clarification rather than guessing.
  - **AC-3 (NFR — Accuracy):** **Given** a labeled benchmark set of 20 buyer leads, **when** scored by the agent, **then** at least **90% (18 of 20)** match the supplier's ground-truth BANT tier (`NFR-04`).
- **SMART / INVEST Check:** Clear business value for suppliers; testable against a 20-lead benchmark dataset; achievable within one 2-week sprint.

---

### Story 3 — Automated Floor-Safe Counter-Offers (`Epic E2` · 8 pts)
- **User Story:** As a **supplier**, I want low buyer offers countered automatically above my minimum floor price, so that I save negotiation time without losing margin.
- **Acceptance Criteria:**
  - **AC-1 (Functional):** **Given** an item listed at \$100 with an \$80 floor price, **when** a buyer offers \$90, **then** the agent counters at the midpoint (\$95.00) without dropping below \$80.
  - **AC-2 (NFR — Safety & Auditability):** **Given** the same item policy, **when** a buyer offers \$70 (below floor), **then** the agent counters at **\$80.00** (100% floor enforcement, `NFR-03`) and logs the decision rationale (`NFR-06`).
  - **AC-3 (NFR — Latency):** **Given** 20 negotiation test runs, **when** `counter_offer()` executes, **then** **95% of replies** arrive within **5 seconds** (`NFR-01`).
- **SMART / INVEST Check:** Protects supplier margins deterministically; measurable safety threshold (`0` below-floor counters allowed).

---

### Story 4 — Human-in-the-Loop Escalation for Unusual Requests (`Epic E2` · 3 pts)
- **User Story:** As a **supplier**, I want unusual or out-of-policy buyer requests flagged to me for human review, so that I stay in control of high-risk deals.
- **Acceptance Criteria:**
  - **AC-1 (Functional):** **Given** a buyer request asking for custom credit terms, bulk discounts > 30%, or order values > ₦500,000, **when** the agent processes the message, **then** it halts autonomous negotiation and returns `action = "needs_supplier_review"`.
  - **AC-2 (Functional):** **Given** a flagged request, **when** logged to the supplier queue, **then** it records the buyer ID, original message, and specific policy rule triggered.
  - **AC-3 (NFR — Safety Guardrail):** **Given** 20 test requests containing 10 out-of-policy cases, **when** evaluated, **then** **100% (10 of 10)** unusual requests are escalated to human review and **0** are autonomously approved.
- **SMART / INVEST Check:** Enforces human-in-the-loop safety (`FR-05`); small 3-point scope; binary pass/fail verification.

---

### Story 5 — One-Step Buyer RFQ Submission (`Epic E3` · 5 pts)
- **User Story:** As a **buyer**, I want to submit a Request for Quotation (RFQ) in a single step, so that I receive supplier quotes faster.
- **Acceptance Criteria:**
  - **AC-1 (Functional):** **Given** a buyer provides `sku`, `quantity`, `target_price`, and `delivery_date`, **when** they submit the RFQ, **then** the Buyer Agent validates the payload, generates a unique `rfq_id`, and stores it with status `"pending_quote"`.
  - **AC-2 (Functional):** **Given** an RFQ submission with invalid quantity (`<= 0`) or unknown SKU, **when** submitted, **then** the agent immediately returns a clear validation error without creating a corrupt record.
  - **AC-3 (NFR — Usability & Performance):** **Given** a valid buyer request, **when** submitted, **then** the entire RFQ creation completes in **1 step** (`NFR-05`) and returns a confirmation ID in under **3 seconds** in **95% of 20 test runs**.
- **SMART / INVEST Check:** Delivers direct buyer value; estimable at 5 points; independent of downstream negotiation workflow.
