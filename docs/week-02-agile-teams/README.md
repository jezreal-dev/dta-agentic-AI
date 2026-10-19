# Week 2: Serving in Agile Teams + Collaboration

> **Module:** Week 2 — Serving in Agile Teams, Sprint Practices, Git & AI-Ready Habits  
> **Companion Guide:** [Git & VS Code Step-by-Step Guide](git-vscode-guide.md) · **Assignment:** [Week 2 Mini Sprint Plan (Story 2.1)](../../assignments/week-02/submission.md)  

---

## Welcome Back to the eComMART AI Squad

**Day 1 of Sprint 1.** The Product Owner has pulled **Story 1.1** (*check stock before quoting*) and **Story 2.2** (*counter low offers automatically*) into the sprint. Everyone starts coding immediately:
- **Muhammad** writes `counter_offer()` and assumes the supplier's floor price sits in a config file.
- **Abdullah** builds `ProductCatalog` and stores the floor price inside each product record.
- Nobody writes a test. Nobody asks who is doing what. Both push straight to the `main` branch at 4:00 PM.
- **By 5:00 PM**, the agent is countering offers at **\$65 on an \$80 floor**. A supplier would lose money on every deal.

> **Root Causes:**
> 1. **Hidden Assumptions & Missing Refinement:** Nobody aligned on the data contract (where the floor price lives).
> 2. **No Version Control Isolation or Peer Review:** Both pushed directly to `main` without branches or a Pull Request review.
> 3. **No Automated Tests / Guardrail Checks:** Neither engineer wrote a floor-price enforcement test (`NFR-03`) before merging.

### Learning Objectives for Week 2
By the end of Week 2, you can:
1. Name the **three Scrum roles** and explain what each one owns.
2. Explain the purpose, time-box, and concrete output of each **Sprint practice**.
3. Break a user story into small, role-tagged **tasks**, verify **coverage**, and spot **dependencies and blockers**.
4. Follow the **Git workflow** from `branch → commit → Pull Request → review → merge`.
5. Apply **four habits for AI delivery**: run experiments, log failure cases, set measurable success criteria, and keep a human in the loop.
6. Produce a complete **Mini Sprint Plan** for an AI-related user story.

---

## Part 1: Working in Agile Teams

An Agile team is a small, cross-functional squad that owns a result together—like a restaurant kitchen where the head chef sets the menu, the expediter keeps orders flowing, and the line cooks prepare the dishes.

### The Three Scrum Roles

| Role | Owns | Typical Question | eComMART Example |
| :--- | :--- | :--- | :--- |
| **Product Owner (PO)** | **The What and the Why:** The product backlog and its priority order | *"Is this the most valuable thing to build next?"* | Decides Story 2.2 comes before Story 3.1 because suppliers are losing negotiation time |
| **Scrum Master (SM)** | **The Process:** Helps the team follow Scrum and removes impediments | *"What is slowing the team down?"* | Notices cards piling up in review and proposes a WIP limit of 2 cards in `In Review` |
| **Developers** | **The How:** Turning stories into a working, tested increment | *"How do we build and prove this works?"* | Designs `counter_offer()`, writes floor-price tests, and measures reply latency |

### Cross-Functional Role Tags ("Hats, Not Walls")
In Scrum, "Developers" includes everyone delivering the increment. On the eComMART squad, every task carries one of six role tags:

| Tag | Focus Area | eComMART Example |
| :---: | :--- | :--- |
| **`DEV`** | Application engineering & code implementation | Writing `check_stock(sku)` and `counter_offer()` |
| **`DATA`** | Preparing and managing schemas & datasets | Building `ProductCatalog` JSON and sample test data |
| **`EVAL`** | Prompts & AI evaluation: measuring how the AI behaves | Counting invented-stock cases and benchmarking latency |
| **`QA`** | Testing that the story meets its Acceptance Criteria | Floor-price enforcement and out-of-stock unit tests |
| **`UX`** | Buyer and supplier user experience | Making an RFQ possible in a single step |
| **`SEC`** | Security and safe handling of secrets | Keeping API keys in `.env` and out of the Git repository |

### Silo Thinking vs. Shared Ownership

| Silo Thinking (Anti-Pattern) | Shared Ownership (eComMART Squad Standard) |
| :--- | :--- |
| *"My function works. I am done."* | *"The story is delivered only when it meets the Definition of Done."* |
| *"QA will catch it."* | *"We build quality in. QA helps us prove it."* |
| *"That is not my task."* | *"What does the Sprint Goal need next?"* |
| Hide a problem until the Sprint Review demo. | Raise risks openly at the next Daily Scrum. |
| `[EVAL]` *"The AI passed my test. My job is done."* | `[EVAL]` *"The AI passed my test. I will log edge cases for QA to confirm."* |

---

## Part 2: Agile Team Practices

Sprint 1 at eComMART is **2 weeks (10 working days)**. Five practices create the squad's rhythm:

| Practice | Purpose | Typical Time-Box (2-wk Sprint) | Concrete Output |
| :--- | :--- | :--- | :--- |
| **Backlog Refinement** | Make upcoming stories clear, sized, and ready (`Definition of Ready`) | Ongoing (~1 hr mid-sprint) | Clarified stories, updated ACs, story point sizes, exposed dependencies |
| **Sprint Planning** | Agree on what to build this sprint and how to deliver it | Up to 2–4 hours (Day 1) | **Sprint Goal** + **Sprint Backlog** (selected stories + task breakdown) |
| **Daily Scrum** | Inspect progress toward the Sprint Goal and surface blockers | **15 minutes** daily | Updated 24-hour plan + visible impediments for the Scrum Master |
| **Sprint Review** | Inspect **WHAT** was built: demo the working increment to stakeholders | ~1 hour (Last day) | PO confirms `Done` stories against ACs + updated Product Backlog from feedback |
| **Sprint Retrospective** | Inspect **HOW** the team worked and improve the process | ~45–60 min (After Review) | 1–2 concrete process improvements (`Stop / Continue / Start`) for the next sprint |

### Retrospective Format: `Stop / Continue / Start`
- **STOP:** Merging without a code review; pushing directly to `main`; hiding blockers until the demo.
- **CONTINUE:** Holding the Daily Scrum at the same time every day; writing Acceptance Criteria before coding.
- **START:** Writing the floor-price test alongside the function; reviewing waiting PRs whenever `In Review` hits its WIP limit of 2.

---

## Part 3: Effective Collaboration

### 1. Slicing Stories into Tasks & The Coverage Test
A good task can be finished in **1–2 days**, has **one owner**, and carries **one role tag**.
Once tasks are drafted, run the **Coverage Test**:
> **Coverage Rule:** Does every Acceptance Criterion (`AC`) have at least **one task that builds it** and **one task that proves it**? If an AC has no matching task, you have caught a gap before writing a single line of code.

### 2. Spotting & Reducing Dependencies

| Dependency Type | eComMART Example | How to Reduce It |
| :--- | :--- | :--- |
| **Task-to-Task** | `counter_offer()` needs stock count from `ProductCatalog` | Build/merge the loader first, or agree on the function signature early |
| **Data** | Floor-price tests need supplier floor prices | Create a small 3-SKU mock/sample JSON catalog so testing can proceed immediately |
| **Decision** | PO must define what counts as an "unusual request" | Ask in Backlog Refinement and document the rule list directly on the story card |
| **Access / Tools** | Team needs a shared GitHub repo before opening PRs | Set up repository access on Day 1 before feature work starts |

### 3. Bad vs. Good Feedback Across Sprint Events
Good feedback is **about the work, not the person**—it is **Specific, Kind, and Actionable** (often phrased as a *question + suggestion*):

| Sprint Event | Unhelpful Feedback | Helpful Feedback (Specific, Kind, Actionable) |
| :--- | :--- | :--- |
| **Sprint Planning** | *"This story is too vague."* | *"AC-2 does not say what counts as a valid counter. Can we add a rule before we commit?"* |
| **Daily Scrum** | *"You should have done that yesterday."* | *"That task has been In Progress for 3 days. Can I help unblock you after the standup?"* |
| **Backlog Refinement** | *"Split it somehow."* | *"If we split at the stock-check boundary, Story A stays at 5 pts and Story B drops to 3."* |
| **Retrospective** | *"Someone kept breaking the build."* | *"Two builds broke from unreviewed merges. Stop: require a passing test before merging."* |
| **Code Review (PR)** | *"I don't like this."* or *"Looks fine."* | *"What happens when `stock` is 0 or negative? Can we add a test case for out-of-stock?"* |

---

## Part 4: Preparing Teams for AI Delivery (The 4 AI-Ready Habits)

### Habit 1: Run Structured Experiments
Treat uncertain AI behavior as a testable hypothesis with a metric and a time-box:
> **Template:** *"We believe `<change>` will achieve `<measurable metric>`, and we will know in `<time-box>`."*  
> **Example:** *"We believe passing stock count into `counter_offer` will cut invented stock to 0 of 20 test cases, and we will know in 2 days."*

### Habit 2: Maintain a Failure Case Log
Whenever the agent produces an incorrect, hallucinated, or unsafe output, record it immediately in a blameless **Failure Case Log**. Every resolved failure becomes a permanent regression test:

| ID | Input | Expected Output | Actual Output | Violated Rule | Severity | Status / Fix |
| :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **F-01** | Listed \$100, Floor \$80, Offer \$70 | Counter $\ge \$80$ | Countered at \$65 | `NFR-03` (Floor safety) | **Critical** | Fixed in code guardrail + added `Test 2` |
| **F-02** | SKU-102 (`stock = 0`), Offer \$85 | Return `"unavailable"` | Countered at \$92.50 | `NFR-02` / `AC-3` | **High** | Added `stock == 0` check on branch + `Test 4` |

### Habit 3: Set Measurable Success Criteria
Avoid subjective goals like *"the AI should feel fast and helpful."* Use objective pass/fail thresholds:
- **Latency (`NFR-01`):** Reply under **5 seconds** in **95% of 20 test runs**.
- **Reliability (`NFR-02`):** **0 invented stock cases** in **20 of 20 test runs**.
- **Safety (`NFR-03`):** **100% enforcement** of supplier floor prices across all test cases.

### Habit 4: Human Validation (Guardrails & Human-in-the-Loop)
Watch out for **automation bias** (trusting an AI answer simply because it sounds fluent and confident). Always verify against the source of truth:

| Stage | Human Role | eComMART Example |
| :--- | :--- | :--- |
| **Before** | Set policies, rules, and hard boundaries | Supplier sets the listed price and minimum floor price |
| **During** | Approve or take over high-risk/out-of-policy cases | Requests outside negotiation rules or > ₦500,000 are flagged for human review (`FR-05`, `AC-4`) |
| **After** | Audit decisions and rationale | Supplier reviews logged negotiation decisions and rationale (`NFR-06`) |

---

## Part 5: Instructor Demo — Story 2.2 from Story to Sprint Execution

Taking **Story 2.2: Counter low offers automatically (8 pts)** through a 6-step Sprint lifecycle:

1. **Step 1 — Refinement (`Definition of Ready` Check):**
   - Clear ACs? **Yes** (`AC-1` to `AC-5`).
   - Sized? **Yes** (`8 pts`).
   - No open dependency? **Not yet**—needs stock count from `ProductCatalog` (Story 1.1).
   - *Key Refinement Decisions:* Counter is midpoint between offer and listed price (never below floor); floor price lives in the product catalog record; `stock == 0` returns `"unavailable"`; out-of-policy requests return `"needs supplier review"`.
2. **Step 2 — Task Breakdown & Coverage Test:**
   - Initial 4 tasks left gaps on `AC-2` (decision logging) and `AC-4` (flagging unsupported requests).
   - **Added 2 tasks via Coverage Test:**
     - `[DEV]` Log each counter decision and its rationale (`AC-2`, `NFR-06`).
     - `[DEV]` Return `"needs supplier review"` for requests outside rules (`AC-4`).
3. **Step 3 — Map Dependencies & Order Work:**
   - Use a 3-SKU sample catalog to unblock `counter_offer()` while `ProductCatalog` JSON loader is being built.
4. **Step 4 — Board & WIP Limits (Day 3 Snapshot):**
   - Enforce `WIP ≤ 2` on `In Progress` and `In Review`. If a developer finishes early and `In Progress` is full, they help **review waiting PRs** first rather than pulling a new card.
5. **Step 5 — Sprint Review against ACs:** Demo `AC-1` through `AC-5` live to the Product Owner.
6. **Step 6 — Definition of Done Check:** Verify code is reviewed & merged to `main`, tests are written & passing, and PO has accepted the demo.

---

## Part 6: In-Session Hands-On Activities & Solutions

### Activity 1: Sprint 1 Kickoff Role-Play (15 min)
- **Sprint Selection:** Story 1.1 (5 pts) + Story 2.2 (8 pts) = **13 points** (leaving a safe buffer below the 20-point velocity for AI uncertainty).
- **Blocker Card Responses:**
  - *Card A (Catalog data not ready):* Use a 3-SKU sample catalog so work continues, and prioritize reviewing the catalog loader today.
  - *Card B (Unusual request undefined):* PO defines a short rule list by end of day and attaches it to the story card.
  - *Card C (3 cards stuck in In Review for 2 days):* Stop pulling new work; swarm on reviews; adopt a 24-hour review rule in the Retrospective.
  - *Card D (Floor-price SME on leave):* Pair up immediately to share knowledge and document the schema on the card.
  - *Card E ("We'll write tests at the end"):* Point to the Definition of Done—add a `QA` task now and write tests alongside code.

### Activity 2: Slice Story 2.3 into Tasks (15 min)
- **Story 2.3:** *As a supplier, I want unusual requests flagged to me, so I stay in control.* (3 pts, Epic E2, `FR-05`)
- **Acceptance Criteria:**
  - **AC-1:** Given a request outside supported negotiation rules, when the agent processes it, then it flags the request to the supplier instead of guessing.
  - **AC-2:** Given a flagged request, when the supplier opens their review list, then the request appears with the buyer's message and the flag reason.
  - **AC-3 (Measurable):** Given 20 test requests including unusual ones, when processed, 100% of unusual requests are flagged and 0 are answered autonomously.
- **Task Plan (Passing Coverage Test):**
  1. `[DATA]` Agree with PO on "unusual request" rule list (`Covers: AC-1`)
  2. `[DEV]` Write function classifying requests as normal vs. `needs_review` (`Covers: AC-1`)
  3. `[DEV]` Store flagged requests with buyer message and reason (`Covers: AC-2`)
  4. `[UX]` Define supplier review list fields and display format (`Covers: AC-2`)
  5. `[QA]` Test normal vs. unusual requests and verify review list fields (`Covers: AC-1, AC-2`)
  6. `[EVAL]` Run 20-request benchmark and verify 100% flag accuracy (`Covers: AC-3`)

---

## Self-Assessment: Sprint Challenge Key Takeaways (12 Questions)

1. **Product Owner** owns the *what* and *why* and orders the backlog.
2. **WIP Limits** stop teams from starting new work when `In Review` is bottlenecked.
3. **Strong Daily Scrum update:** Names what was finished, what is next, and the specific blocker.
4. **Retrospective** is where the team agrees on process improvements (e.g., a 24-hour PR review rule).
5. **Definition of Ready (DoR):** Clear ACs, sized, no open blocking dependency.
6. **Well-sized task:** `[QA] Test floor-price enforcement` (small, role-tagged, verifiable).
7. **Reducing a dependency:** Use a small sample catalog while the full loader is in progress.
8. **Pull Request purpose:** Propose merging a branch and open a space for peer code review.
9. **Measurable criterion:** *"No invented stock in 20 of 20 test cases."*
10. **Out-of-policy request (e.g., 40% discount):** Flag it for supplier review (`AC-4`, `FR-05`).
11. **Failure Case Log purpose:** Each fixed failure becomes a permanent regression test and reveals systemic patterns without blame.
12. **Below-floor counter (\$65 on \$80 floor):** Log as **Critical**, fix code guardrail, and add a permanent regression test.
