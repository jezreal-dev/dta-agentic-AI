# Week 1: Agile Fundamentals & The eComMART AI Squad

> **Module:** Week 1 — Agile Fundamentals & Welcome to the Team  
> **Case Study:** **eComMART** (Multinational B2B Marketplace)  
> **Related Slides:** [Week 1 Presentation Breakdown](slides-summary.md) · **Assignment:** [Week 1 Takeaway Exercise](../../assignments/week-01/README.md)  

---

## 1. The Scenario: Welcome to eComMART!

You have just landed a role on eComMART's newly formed **AI Engineering Squad**. eComMART is a multinational B2B marketplace experiencing rapid growth. As platform traffic surges, manual operations are breaking down:
- **Buyers** wait too long to receive responses and quotes.
- **Suppliers** are exhausted from manually qualifying leads, checking stock, and answering repetitive price negotiations.

### The 24-Week Squad Mission
Over the next 24 weeks, your squad will build a modern **Agentic Commerce System** powered by two AI agents:
1. **The Buyer Agent:** Acts as a procurement assistant—helping buyers find products, check stock, submit **RFQs** (Requests for Quotation) in one step, and negotiate prices.
2. **The Seller Agent:** Acts as a virtual storefront assistant for independent suppliers—checking live inventory, qualifying leads using standard business frameworks (**BANT**), automatically replying to buyer negotiations within safe floor-price boundaries, and escalating unusual requests to a human.

### Why Agile for AI?
In traditional software delivery (**Waterfall**), teams write a massive upfront specification, spend months coding in isolation, and deploy at the end. When enterprises tried building AI systems this way, it failed because **AI behavior is probabilistic and unpredictable**—models hallucinate, data is messy, and rigid upfront plans fail on day one.

To build production AI in industry, teams use **Agile**:
- Work in small, verifiable timeboxes (**Sprints**).
- Separate **Functional Requirements** (*what the system does*) from **Non-Functional Requirements** (*how well and safely it behaves*).
- Continuously run the AI delivery loop: $\text{Experiment} \longrightarrow \text{Evaluate} \longrightarrow \text{Improve}$.

---

## 2. Worked Case Study: The eComMART Product Backlog

### Epics
Every backlog begins with ambitious, high-level goals that span multiple sprints:

| ID | Epic | Business Outcome | Colour Tag |
| :---: | :--- | :--- | :---: |
| **E1** | **Seller Agent Checks Inventory** | Suppliers never quote items they do not have | Blue |
| **E2** | **Lead Qualification and Negotiation** | Qualify leads and counter offers safely | Teal |
| **E3** | **Buyer Agent Speeds Up RFQs** | Buyers submit and track RFQs faster | Orange |

---

### User Stories (All 7 Stories)
Each Epic splits into small, independently testable slices of value estimated in Fibonacci **Story Points**:

| ID | Epic | User Story (`As a... I want... so that...`) | Points | Priority / Target |
| :---: | :---: | :--- | :---: | :--- |
| **1.1** | **E1** | As a **supplier**, I want the Seller Agent to check my stock before quoting, so that I never promise items I do not have. | **5** | Must · Sprint 1 (MVP) |
| **1.2** | **E1** | As a **buyer**, I want instant answers on stock, so I can plan my purchase. | **3** | Should · Sprint 2 |
| **2.1** | **E2** | As a **supplier**, I want leads scored on Budget, Authority, Need and Timeline (**BANT**), so I focus on serious buyers. | **5** | Should · Sprint 2 |
| **2.2** | **E2** | As a **supplier**, I want low offers countered automatically, so I save negotiation time. | **8** | Must · Sprint 1 (MVP) |
| **2.3** | **E2** | As a **supplier**, I want unusual requests flagged to me, so I stay in control. | **3** | Should · Sprint 2 |
| **3.1** | **E3** | As a **buyer**, I want to submit an RFQ in one step, so I get quotes faster. | **5** | Could · Sprint 3 |
| **3.2** | **E3** | As a **buyer**, I want to check my RFQ status, so I do not have to chase suppliers. | **3** | Could · Sprint 3 |

---

### Engineering Tasks (Sprint 1 Stories)
Role tags used across the squad:
- `DEV`: Application engineering
- `DATA`: Data preparation & catalog schemas
- `EVAL`: Prompt & AI behavior evaluation
- `QA`: Quality assurance & acceptance testing
- `UX`: Buyer and supplier experience
- `SEC`: Security & secret handling

| Story | Sprint 1 Tasks |
| :--- | :--- |
| **Story 1.1** *(Check stock before quoting)* | • `[DEV]` Write `check_stock(sku)`<br>• `[DEV]` `ProductCatalog` loads JSON<br>• `[QA]` Test stock availability scenarios<br>• `[EVAL]` Measure reply time and invented-stock cases |
| **Story 2.2** *(Counter low offers automatically)* | • `[DEV]` Write `counter_offer(listed, offer, floor, stock)`<br>• `[DEV]` Pass stock count into `counter_offer`<br>• `[QA]` Test floor-price enforcement<br>• `[EVAL]` Test invented prices and response latency |

---

## 3. Functional vs. Non-Functional Requirements

### Functional Requirements (What the System Does)

| ID | Requirement | Linked Story |
| :---: | :--- | :---: |
| **FR-01** | Check the `ProductCatalog` for the requested SKU before quoting | Story 1.1 |
| **FR-02** | Return true stock availability for the requested SKU | Story 1.1 |
| **FR-03** | Counter low offers using listed price, offer, floor price, and stock | Story 2.2 |
| **FR-04** | Never counter below the supplier's floor price | Story 2.2 |
| **FR-05** | Flag unusual requests to the supplier for human review | Story 2.3 |
| **FR-06** | Score leads using Budget, Authority, Need, and Timeline (**BANT**) | Story 2.1 |
| **FR-07** | Allow buyers to submit an RFQ in one step | Story 3.1 |
| **FR-08** | Allow buyers to check RFQ status | Story 3.2 |

### Non-Functional Requirements (How Well It Does It — With Measurable Targets)

| ID | Theme | Measurable Requirement | Linked Story |
| :---: | :--- | :--- | :---: |
| **NFR-01** | **Performance** | Reply under **5 s** in **95% of 20 test runs** | Story 1.1, Story 2.2 |
| **NFR-02** | **Reliability** | **No invented stock** in **20 of 20 test cases** | Story 1.1 |
| **NFR-03** | **Safety** | Counter **never falls below** the supplier floor price | Story 2.2 |
| **NFR-04** | **Accuracy** | Lead scoring follows **BANT** consistently on the test set | Story 2.1 |
| **NFR-05** | **Usability** | Buyer can submit an RFQ in **one step** | Story 3.1 |
| **NFR-06** | **Auditability** | Negotiation decisions and rationale can be reviewed by the supplier | Story 2.2 |

---

## 4. Acceptance Criteria (`Given / When / Then`)

### Story 2.2: Counter low offers automatically
*Sample policy: Floor price \$80 on a \$100 listed item.*

- **AC-1 (Within floor):** **Given** an item is listed at \$100 with a floor price of \$80, **when** a buyer offers \$90, **then** the agent sends an acceptable counter without going below the \$80 floor.
- **AC-2 (Floor protection):** **Given** the same policy, **when** a buyer offers \$70, **then** the agent never counters below \$80 and logs the decision.
- **AC-3 (Stock-aware response):** **Given** 3 units are in stock, **when** a buyer makes a low offer, **then** the agent uses the available stock when generating the counter.
- **AC-4 (Human control):** **Given** a request is outside the supported negotiation rules, **when** the agent processes it, **then** it flags the request for supplier review instead of guessing.
- **AC-5 (Latency):** Each negotiation reply arrives within **5 s in 95% of 20 test runs**.

### Story 1.1: Check stock before quoting

- **AC-1:** **Given** an SKU in the `ProductCatalog`, **when** a supplier requests a quote, **then** the agent returns the true stock availability.
- **AC-2:** **Given** an SKU with insufficient stock, **when** a buyer requests it, **then** the agent does not invent availability.
- **AC-3:** **Given** 20 test runs, **no invented stock** appears in **20 of 20 cases**.

---

## 5. Core Agile Glossary (with eComMART Examples)

| Term | Meaning | eComMART Example |
| :--- | :--- | :--- |
| **Product Backlog** | Ordered list of everything the product may need, owned by the Product Owner | All 7 stories (`1.1`–`3.2`) before planning |
| **Sprint** | Fixed time-box (1–4 weeks) that ends with a usable increment | Sprint 1 = 2 weeks (10 working days) |
| **Sprint Goal** | One-sentence purpose of the sprint | *"Seller Agent checks stock and counters offers safely"* |
| **Sprint Backlog** | Items the team commits to for the sprint, plus the plan to deliver them | Story 1.1 + Story 2.2 (13 pts total) |
| **Spike** | Time-boxed research to cut uncertainty; output is knowledge, not a shippable feature | Researching LLM hallucination rates before building a prompt |
| **Story Points** | Relative size covering effort, complexity, and uncertainty (Fibonacci: 1, 2, 3, 5, 8, 13) | Story 1.1 = 5 pts; Story 2.2 = 8 pts |
| **Velocity** | Points finished per sprint, used for forecasting | Team average: 20 pts per sprint |
| **Lanes (Columns)** | Workflow stages a card moves through on the board | `Backlog → To Do → In Progress → In Review → Done` |
| **WIP Limit** | Cap on cards per lane, to stop starting more than you finish | `In Progress ≤ 2`; `In Review ≤ 2` |
| **Definition of Ready (DoR)** | Checklist a story must meet before entering a sprint | Clear ACs, sized, no open blocking dependency |
| **Definition of Done (DoD)** | Team-wide quality bar for every story | Code reviewed and merged · Tests written and passing · Demoed to the Product Owner |
| **Acceptance Criteria (AC)** | Pass/fail conditions specific to one story | `AC-1` to `AC-5` of Story 2.2 |
| **Impediment / Blocker** | Anything blocking progress, raised in the Daily Scrum | Waiting for `ProductCatalog` JSON data |
| **Ceremonies** | Sprint Planning, Daily Scrum, Sprint Review, Retrospective (plus Backlog Refinement) | 2-week cadence events |
| **Roles** | Product Owner (*what & why*), Scrum Master (*process*), Developers (*how*) | Cross-functional squad |
| **Guardrail / Human-in-the-loop** | Agent-specific: hard limits that force escalation to a person | The \$80 floor-price rule and flagging unusual requests in Story 2.2 |

---

## 6. Scrum & Kanban Board Specifications

### Scrum Board Snapshot (Sprint 1 — Day 5 of 10)
- **Sprint Goal:** *"Seller Agent checks stock and counters offers safely."*
- **Metrics:** Day 5 of 10 · Committed: **13 pts** · Done: **0 pts** · Historical Velocity: **20 pts**
- **Sprint 1 Stories:** Story 1.1 (5 pts) + Story 2.2 (8 pts)
- **Product Backlog (Future Sprints):** Story 1.2, Story 2.1, Story 2.3, Story 3.1, Story 3.2

### Kanban Board Snapshot
- **Workflow Lanes (5):** `Backlog` | `To Do` | `In Progress (WIP ≤ 2)` | `In Review (WIP ≤ 2)` | `Done`
- **State:**
  - **Backlog:** Story 1.2, Story 2.1, Story 2.3, Story 3.1, Story 3.2
  - **To Do:** *(Empty)*
  - **In Progress (2/2 FULL):** Story 1.1, Story 2.2
  - **In Review:** *(Empty)*
  - **Done:** *(Empty)*
- **Pull Principle:** Because `In Progress` is at its WIP limit of 2, no developer may pull Story 1.2 until either Story 1.1 or Story 2.2 moves forward and frees a slot.
