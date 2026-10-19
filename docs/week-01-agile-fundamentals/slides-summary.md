# Week 1 Presentation Summary: Agile Fundamentals

> **Instructor:** Mudit Khetan  
> **Session Duration:** 2 Hours  
> **Companion Guide:** [Week 1 Agile Fundamentals Guide](README.md)  

---

## Session Agenda
1. **The eComMART Story:** Meet the squad and the AI commerce mission.
2. **Module 1 — Agile Fundamentals:** Mindset, Waterfall vs. iterative delivery, Scrum, and Kanban.
3. **Module 2 — Core Agile Workflow:** Epics, User Stories, SMART criteria, FR vs. NFR, Sprints, and Definition of Done.
4. **Module 3 — Agile Transformation:** Product-oriented vs. project-oriented teams, cross-functional squads, and feedback loops.
5. **Module 4 — Agile for AI Projects:** Why AI features require experiments (`Experiment → Evaluate → Improve`), not fixed specifications.
6. **Live Demo & Takeaway:** Building a real backlog together from scratch.

---

## Module 1: Agile Fundamentals

### Evolution & History of Agile
- **1950s:** Kanban visual workflow pioneered at Toyota.
- **1970:** Waterfall model described (months of upfront planning, built in isolation, expensive surprises at launch).
- **1995:** Scrum framework presented.
- **2001:** The **Agile Manifesto** written.
- **Today:** Agile is the industry standard for handling uncertainty and rapid iteration.

### The 4 Core Agile Values
1. **Individuals & Interactions** over rigid processes and tools.
2. **Working Software** (a usable increment) over comprehensive documentation.
3. **Customer Collaboration** (buyers and suppliers shaping the plan with us) over contract negotiation.
4. **Responding to Change** (adjusting the plan as we learn more) over following a fixed plan.

### The 12 Agile Principles (Applied to the eComMART Squad)
1. **Early & Continuous Delivery:** Deliver value early—a working stock check beats a theoretical plan.
2. **Welcome Change:** Late changes are welcome—a new RFQ rule is useful input, not a threat.
3. **Deliver Frequently:** Ship working software every few weeks, not every few months.
4. **Business + Devs Together:** The Product Owner and engineers collaborate daily.
5. **Motivated Individuals:** Give the squad support and trust instead of micromanaging.
6. **Face-to-Face Conversation:** Direct, real-time conversation beats long email threads.
7. **Working Software = Progress:** Demo real working features, not slide status reports.
8. **Sustainable Pace:** A steady, repeatable sprint rhythm beats heroic late nights.
9. **Technical Excellence:** Clean code and good design keep future changes cheap.
10. **Simplicity:** Maximize the amount of work *not* done—build only what is needed for the current goal.
11. **Self-Organizing Teams:** The squad decides *how* to build; the best architectures emerge from the team.
12. **Reflect & Adjust:** Hold regular retrospectives and tune how the team works.

### Waterfall vs. Iterative (Agile) Delivery

| Dimension | Waterfall | Iterative (Agile) |
| :--- | :--- | :--- |
| **Planning** | Plan everything upfront in a massive spec | Plan just enough to start the next slice |
| **Execution** | Build for months untested in isolation | `Plan → Design → Build → Test → Review → Release` |
| **Release & Risk** | One big release at the end; high risk | Release often, learn fast via continuous feedback loop |
| **Attitude to Change** | Change is expensive and resisted | Change is expected and welcomed |

### Scrum vs. Kanban: When to Use Which

| Framework | Key Characteristics | Best Suited For |
| :--- | :--- | :--- |
| **Scrum** | • Fixed-length sprints (1–4 weeks)<br>• Ceremonies: Plan, Daily Scrum, Review, Retro<br>• Roles: Product Owner, Scrum Master, Developers | Coordinated feature releases and structured product milestones |
| **Kanban** | • Continuous flow (no fixed sprints)<br>• Strict **WIP (Work-in-Progress) limits** per column<br>• Pull new work only when capacity frees up | Ongoing operations, support queues, and continuous delivery |

> **Industry Practice:** Most real engineering teams blend both (**"Scrumban"**)—using Scrum's cadence for planning/reviews and Kanban's visual board + WIP limits for daily execution.

---

## Module 2: Core Agile Workflow

### The Hierarchy: `Epic → User Story → Task`
- **Epic:** A large business goal spanning multiple sprints (e.g., *Epic 1: Seller Agent Checks Inventory*).
- **User Story:** One slice of user value that fits inside a single sprint (e.g., *Story 1.1: Check stock before quoting*).
- **Tasks:** Concrete engineering work taking hours to a couple of days:
  - `1.1.a [FR]` Write `check_stock(sku)`
  - `1.1.b [FR]` `ProductCatalog` loads JSON
  - `1.1.c [NFR]` Reply under 5 s in 95% of 20 runs
  - `1.1.d [NFR]` No invented stock, 20 of 20 cases

### Applying the SMART Criteria to Stories
Every User Story and Acceptance Criterion must be verifiable:
- **S — Specific:** Reads stock from the `ProductCatalog` JSON for every quote.
- **M — Measurable:** Reply under 5 s in 95% of 20 test runs; no invented stock in 20/20 cases.
- **A — Achievable:** One function (`check_stock(sku)`) buildable within one sprint.
- **R — Relevant:** Directly supports Epic 1 (*suppliers never quote items they do not have*).
- **T — Time-bound:** Demoed at the Sprint 1 Review.

### Sorting eComMART Requirements (Functional vs. Non-Functional)

| Requirement Statement | Classification | Why? |
| :--- | :---: | :--- |
| Seller Agent checks live inventory before replying | **Functional (FR)** | Defines a core system behavior/action |
| Quote replies arrive within 5 seconds | **Non-Functional (NFR)** | Defines a performance/latency threshold |
| Every negotiation decision is logged for audit | **Non-Functional (NFR)** | Defines auditability and compliance |
| Buyer Agent submits an RFQ to a supplier | **Functional (FR)** | Defines a user-facing feature |
| Fabricated prices in replies stay below 2% | **Non-Functional (NFR)** | Defines AI reliability/hallucination bounds |
| Lead is scored using a standard business framework (BANT) | **Functional (FR)** | Defines business logic behavior |

### Acceptance Criteria (AC) vs. Definition of Done (DoD)
- **Acceptance Criteria:** Story-specific `Given / When / Then` conditions showing *what must be built* for a particular story to pass.
- **Definition of Done:** A single, team-wide checklist applied to *every* story in *every* sprint:
  1. Code reviewed and merged
  2. Tests written and passing
  3. Demoed to the Product Owner

---

## Module 3: Agile Transformation

### Project-Oriented vs. Product-Oriented Delivery

| Project-Oriented Mindset | Product-Oriented Mindset (eComMART Squad) |
| :--- | :--- |
| Temporary team forms, ships, and disbands | Long-lived squad owns the product end-to-end |
| Success = delivered "on time and on budget" | Success = measurable business value delivered to users |
| Handed off to maintenance once "done" | Continuously improved after launch based on real usage |
| Scope locked upfront | Scope evolves with user feedback and AI evaluation data |

---

## Module 4: Agile for AI Projects

### Prototype vs. Production-Ready AI
- **Prototype:** Proves the idea can work at all; hand-checked on a small sample of cases; rough around the edges; goal is to **learn fast**.
- **Production-Ready:** Handles messy real-world inputs; tested, monitored, and logged; fails gracefully with human-in-the-loop guardrails; goal is **trust at scale**.
- **Rule of Thumb:** Every AI feature starts as a prototype—never skip straight to production without evaluation.

### The AI Delivery Loop: `Experiment → Evaluate → Improve`
Because AI outputs are probabilistic, teams manage uncertainty through four steps:
1. **Define a Hypothesis:** *"If the agent uses inventory data, hallucinated stock replies drop to 0 in 20 test cases."*
2. **Measure with Test Cases:** Run against a fixed benchmark set of real examples so results are comparable.
3. **Human Validation:** A person reviews flagged or high-stakes outputs before trusting the system.
4. **Capture Failures:** Every bad output or hallucination is logged and converted into a permanent regression test case.

---

## Live Demo Summary: Building the MVP Backlog

During the live session, the squad prioritized the 7 stories into a 3-Sprint roadmap using **MoSCoW** prioritization:

1. **Sprint 1 — MVP (Must Have · 13 pts · 9 tasks):**
   - *Goal:* Seller Agent checks stock and counters offers safely.
   - Stories: **Story 1.1** (5 pts) + **Story 2.2** (8 pts).
2. **Sprint 2 — Next (Should Have · 11 pts):**
   - *Goal:* Answer inquiries, score leads, flag the unusual.
   - Stories: **Story 1.2** (3 pts) + **Story 2.1** (5 pts) + **Story 2.3** (3 pts).
3. **Sprint 3 — Later (Could Have · 8 pts):**
   - *Goal:* The Buyer Agent speeds up RFQs.
   - Stories: **Story 3.1** (5 pts) + **Story 3.2** (3 pts).
