# Digital Training Academy (DTA) — Agentic AI in Software Development

[![Program](https://img.shields.io/badge/Program-DTA%20Agentic%20AI%20(Advanced)-0A66C2?style=for-the-badge)](https://dta.education.gov.ng/learners/dashboard)
[![Initiative](https://img.shields.io/badge/Initiative-FME%20%7C%20NESRI-008751?style=for-the-badge)](https://dta.education.gov.ng)
[![Platform](https://img.shields.io/badge/Learning%20Hub-Pluralsight-F15B2A?style=for-the-badge)](https://app.pluralsight.com/channels/details/ef7cfa5a-4fd4-41d7-99f4-44aada048e1f)
[![Schedule](https://img.shields.io/badge/Live%20Classes-Tuesdays%20(24%20Weeks)-6C5CE7?style=for-the-badge)](#24-week-curriculum--progress-tracker)

> **Learner:** Jezreal Momoh  
> **Track:** Agentic AI (Advanced) — *Agentic AI in Software Development Academy (Oct – Mar)*  
> **Assigned Mentor:** Ogiugo Mike  
> **Sponsoring Body:** Federal Ministry of Education (FME) — Nigeria Education Sector Renewal Initiative (NESRI)  
> **Channel Lead (Pluralsight):** Emilie Jones  

---

## Overview

Welcome to the central monorepo for the **24-Week Agentic AI in Software Development Academy**. This repository serves as:

1. **Course Documentation & Knowledge Base:** Clean, structured Markdown guides synthesized from weekly instructor-led sessions, slide decks, and participant guides.
2. **Assignments & Sprint Artifacts:** Weekly takeaway deliverables, user stories, acceptance criteria, and mini sprint plans.
3. **The `eComMART` Multi-Agent Codebase:** Progressive engineering of the **Seller Agent** and **Buyer Agent**—from foundational Python tools and SQLite memory to AWS Bedrock and Claude-powered autonomous agents.
4. **Continuous Learning Hub:** Study notes and lab implementations aligned with the Pluralsight learning channel.

---

## The Overarching Storyline: The `eComMART` AI Squad

Throughout this 24-week program, we operate as engineers on the newly formed **AI Engineering Squad** at **eComMART**, a rapidly scaling multinational B2B marketplace.

### The Business Problem
As eComMART grows, two major bottlenecks threaten the marketplace:
- **Buyers** wait too long to receive responses and quotes for their orders.
- **Suppliers** are overwhelmed manually checking stock, qualifying leads, and answering repetitive price negotiations.

### Our 24-Week Engineering Mission
Build a modern, production-ready **Agentic Commerce System** powered by two collaborative AI agents:

| Agent | Role | Core Capabilities |
| :--- | :--- | :--- |
| **Seller Agent** | Virtual Storefront Assistant for Suppliers | Checks live inventory (`ProductCatalog`), qualifies incoming buyer leads using the **BANT** framework (Budget, Authority, Need, Timeline), automatically counters low offers above floor prices, and flags unusual requests for human review. |
| **Buyer Agent** | Procurement Assistant for Buyers | Helps buyers discover products, check real-time availability, submit one-step **RFQs** (Requests for Quotation), track RFQ status, and negotiate prices. |

---

## Repository Architecture

```text
dta-agentic-AI/
├── README.md                                 # Master Monorepo Overview & Progress Tracker
├── LICENSE                                   # Repository License
├── curriculum/                               # 24-Week Syllabus & Platform Alignment
│   ├── roadmap-24-weeks.md                   # Detailed weekly narrative & technical syllabus
│   └── pluralsight-alignment.md              # Pluralsight courses & DTA dashboard tracker
├── docs/                                     # Structured Weekly Courseware & Guides (Markdown)
│   ├── week-01-agile-fundamentals/           # Week 1: Agile Mindset, Epics, SMART Stories, FR/NFR
│   │   ├── README.md                         # Full Week 1 Study Guide & Worked eComMART Examples
│   │   └── slides-summary.md                 # Complete Week 1 Presentation Breakdown
│   └── week-02-agile-teams/                  # Week 2: Scrum Roles, Sprint Practices, Git, AI Habits
│       ├── README.md                         # Full Week 2 Participant Guide & In-Session Activities
│       └── git-vscode-guide.md               # Step-by-Step Git, Branching, PR & Code Review Guide
├── assignments/                              # Weekly Takeaway Exercises & Submissions
│   ├── week-01/                              # Week 1: 5 User Stories + INVEST/SMART & NFRs
│   │   └── README.md
│   └── week-02/                              # Week 2: Mini Sprint Plan (Story 2.1 - BANT Lead Scoring)
│       ├── assignment-brief.md               # Instructions, rules, and self-check rubric
│       ├── template.md                       # Reusable Mini Sprint Plan template
│       └── submission.md                     # Completed Mini Sprint Plan for Story 2.1 (Epic E2)
├── projects/                                 # eComMART Agentic Commerce System Source Code
│   ├── README.md                             # System architecture & agent specifications
│   ├── seller-agent/                         # Seller Agent tools (check_stock, counter_offer, BANT)
│   ├── buyer-agent/                          # Buyer Agent tools (submit_rfq, get_rfq_status)
│   └── shared/                               # Shared data models, sample catalogs, utilities
├── labs/                                     # Weekly Hands-On Coding Labs & Sandboxes
│   ├── README.md
│   └── week-02-git-practice/                 # Week 2 Git workflow lab (counter_offer.py)
└── notes/                                    # Personal Learning Journal
    ├── tuesday-sessions/                     # Live Tuesday instructor-led class notes
    └── pluralsight/                          # Self-paced Pluralsight module notes
```

---

## 24-Week Curriculum & Progress Tracker

### Phase 1: Building the Engine (Weeks 1 – 6)
*Before connecting LLMs, we build the deterministic "hands" (functions), "memory" (databases), and engineering safety nets (Agile, Git, Pytest) required for reliable AI systems.*

| Week | Module / Theme | eComMART Squad Milestone | Documentation | Assignment Status |
| :---: | :--- | :--- | :--- | :---: |
| **01** | **Agile Fundamentals & Welcome to the Team** | Turn vague boss idea into Epics (`E1`–`E3`), 7 SMART User Stories, FRs/NFRs, and Scrum/Kanban boards | [Week 1 Guide](docs/week-01-agile-fundamentals/README.md) · [Slides](docs/week-01-agile-fundamentals/slides-summary.md) | [Completed](assignments/week-01/README.md) |
| **02** | **Serving in Agile Teams & Collaboration** | Run Sprint 1, slice stories into tagged tasks (`DEV`, `DATA`, `EVAL`, `QA`, `UX`, `SEC`), Git PR flow, 4 AI-ready habits | [Week 2 Guide](docs/week-02-agile-teams/README.md) · [Git Guide](docs/week-02-agile-teams/git-vscode-guide.md) | [Completed (Story 2.1)](assignments/week-02/submission.md) |
| **03** | **Python 3 Foundations — Giving the AI "Hands"** | Build structured dictionary/JSON outputs and reusable tool functions | *Upcoming* | *Pending* |
| **04** | **Python OOP — Organizing the Mess** | Build `ProductCatalog` class reading JSON inventory & handling file errors | *Upcoming* | *Pending* |
| **05** | **Databases — Giving the AI "Memory"** | Migrate from flat files to persistent SQLite storage for orders & inventory | *Upcoming* | *Pending* |
| **06** | **Pro Code — Testing & Environments** | Virtual environments (`venv`), `.env` secret security, and `pytest` suites for agent tools | *Upcoming* | *Pending* |

### Phases 2 – 4: LLM Integration, AWS Bedrock & Claude Agent Development (Weeks 7 – 24)
- **Phase 2 (Weeks 7–12):** Prompt Engineering, Deterministic Evaluation (`EVAL`), Guardrails, and Tool Calling.
- **Phase 3 (Weeks 13–18):** AWS Bedrock Foundations, Knowledge Bases (RAG), and Claude Model Integration.
- **Phase 4 (Weeks 19–24):** Multi-Agent Orchestration (Buyer Agent ↔ Seller Agent), Security (`SEC`), Latency Optimization, and Capstone Demo.

*(See [curriculum/roadmap-24-weeks.md](curriculum/roadmap-24-weeks.md) for the full breakdown).*

---

## Pluralsight & DTA Portal Progress

| Course / Module | Platform | Status | Notes / Reference |
| :--- | :--- | :---: | :--- |
| **Serving in Agile Teams** | DTA / Pluralsight | In Progress (~32%) | [Week 2 Guide](docs/week-02-agile-teams/README.md) |
| **Agile Transformation: Organizational Agility** | Pluralsight | Assigned | [Week 1 Guide](docs/week-01-agile-fundamentals/README.md) |
| **Python 3: The Big Picture** | Pluralsight | Assigned | [Pluralsight Alignment](curriculum/pluralsight-alignment.md) |
| **Python 3 Fundamentals** | Pluralsight | Assigned | [Pluralsight Alignment](curriculum/pluralsight-alignment.md) |

---

## Quick Start: Running the Code Labs

To run the Week 2 Seller Agent negotiation tool locally:

```bash
python3 projects/seller-agent/counter_offer.py
```

---

## Core Agile & AI Engineering Standards (Team Rules)

1. **Golden Git Rule:** Never commit directly to `main` during feature sprints. Always follow `branch → work → test → Pull Request → review → merge`.
2. **Coverage Rule:** Every Acceptance Criterion (`AC`) must have both a **build task** and a **proof task**.
3. **4 AI-Ready Habits:**
   - **Run Experiments:** Frame changes with a clear hypothesis, metric, and time-box.
   - **Log Failure Cases:** Record every hallucination or rule violation immediately to feed the regression test suite.
   - **Measurable Success Criteria:** Pair every AI capability with a verifiable number (e.g., *< 5s latency in 95% of 20 runs*, *0/20 invented stock*).
   - **Human in the Loop:** Enforce hard code guardrails (such as floor-price enforcement) and escalate out-of-policy requests to a human reviewer.
