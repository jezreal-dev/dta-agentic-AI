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
2. **Assignments & Sprint Artifacts:** Weekly takeaway deliverables, user stories, acceptance criteria, mini sprint plans, and Python exercises.
3. **The `eComMART` Multi-Agent Codebase:** Progressive engineering of the **Seller Agent** and **Buyer Agent**—from foundational Python tools and SQLite memory to AWS Bedrock and Claude-powered autonomous agents.
4. **Continuous Learning Hub:** Study notes and lab implementations aligned with the Pluralsight learning channel and official weekly shared links.

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
| **Seller Agent** | Virtual Storefront Assistant for Suppliers | Checks live inventory (`ProductCatalog`), qualifies incoming buyer leads using the **BANT** framework (Budget, Authority, Need, Timeline), automatically counters low offers above floor prices, validates orders, and flags unusual requests for human review. |
| **Buyer Agent** | Procurement Assistant for Buyers | Helps buyers discover products, check real-time availability, submit one-step **RFQs** (Requests for Quotation), track RFQ status, and negotiate prices. |

---

## Repository Architecture

```text
dta-agentic-AI/
├── README.md                                 # Master Monorepo Overview & Progress Tracker
├── LICENSE                                   # Repository License
├── curriculum/                               # 24-Week Syllabus, Shared Links & Platform Alignment
│   ├── roadmap-24-weeks.md                   # Detailed weekly narrative & technical syllabus
│   ├── pluralsight-alignment.md              # Pluralsight courses & DTA dashboard tracker
│   └── shared-resources.md                   # Official weekly Google Docs, Slides, Canva & Drive links
├── docs/                                     # Structured Weekly Courseware & Guides (Markdown)
│   ├── week-01-agile-fundamentals/           # Week 1: Agile Mindset, Epics, SMART Stories, FR/NFR
│   │   ├── README.md                         # Full Week 1 Study Guide & Worked eComMART Examples
│   │   └── slides-summary.md                 # Complete Week 1 Presentation Breakdown
│   ├── week-02-agile-teams/                  # Week 2: Scrum Roles, Sprint Practices, Git, AI Habits
│   │   ├── README.md                         # Full Week 2 Participant Guide & In-Session Activities
│   │   └── git-vscode-guide.md               # Step-by-Step Git, Branching, PR & Code Review Guide
│   └── week-03-python-fundamentals/          # Week 3: Python 3 Foundations — Giving the AI "Hands"
│       ├── README.md                         # Master Index of 25 Python Lessons & Worked Examples
│       ├── img/                              # Visual diagrams for Python concepts
│       ├── 01 - Introduction to Python/      # Lessons 001 – 005
│       ├── 02 - Variables, Literals and Constants/ # Lessons 006 – 009
│       ├── 03 - Programming Building Blocks/ # Lessons 010 – 025 (Operators, Loops, Functions, Collections)
│       ├── 04 - Worked Examples/             # 6 Complete eCOMMart Programs (up to Mini Agent Tool)
│       └── 05 - Exercises/                   # 12 Graded Exercises & Reference Solutions
├── assignments/                              # Weekly Takeaway Exercises & Submissions
│   ├── week-01/                              # Week 1: 5 User Stories + INVEST/SMART & NFRs
│   │   └── README.md
│   ├── week-02/                              # Week 2: Mini Sprint Plan (Story 2.1 - BANT Lead Scoring)
│   │   ├── assignment-brief.md               # Instructions, rules, and self-check rubric
│   │   ├── template.md                       # Reusable Mini Sprint Plan template
│   │   └── submission.md                     # Completed Mini Sprint Plan for Story 2.1 (Epic E2)
│   └── week-03/                              # Week 3: 12 eCOMMart Python Exercises & Solutions
│       ├── README.md
│       ├── exercises.md
│       └── solutions.md
├── projects/                                 # eComMART Agentic Commerce System Source Code
│   ├── README.md                             # System architecture & agent specifications
│   ├── seller-agent/                         # Seller Agent tools (counter_offer.py, mini_agent_tool.py)
│   ├── buyer-agent/                          # Buyer Agent tools (submit_rfq, get_rfq_status)
│   └── shared/                               # Shared data models, sample catalogs, utilities
├── labs/                                     # Weekly Hands-On Coding Labs & Live Session Demos
│   ├── README.md
│   └── week-03-python-fundamentals/          # Week 3 Cohort 1 live demos (001.py–004.py) & Mini Agent Tool
└── notes/                                    # Personal Learning Journal
    ├── tuesday-sessions/                     # Live Tuesday instructor-led class notes
    └── pluralsight/                          # Self-paced Pluralsight module notes
```

---

## 24-Week Curriculum & Progress Tracker

### Phase 1: Building the Engine (Weeks 1 – 6)
*Before connecting LLMs, we build the deterministic "hands" (functions), "memory" (databases), and engineering safety nets (Agile, Git, Pytest) required for reliable AI systems.*

| Week | Module / Theme | eComMART Squad Milestone | Documentation & Resources | Assignment Status |
| :---: | :--- | :--- | :--- | :---: |
| **01** | **Agile Fundamentals & Welcome to the Team** | Turn vague boss idea into Epics (`E1`–`E3`), 7 SMART User Stories, FRs/NFRs, and Scrum/Kanban boards | [Week 1 Guide](docs/week-01-agile-fundamentals/README.md) · [Slides](docs/week-01-agile-fundamentals/slides-summary.md) | [Completed](assignments/week-01/README.md) |
| **02** | **Serving in Agile Teams & Collaboration** | Run Sprint 1, slice stories into tagged tasks (`DEV`, `DATA`, `EVAL`, `QA`, `UX`, `SEC`), Git PR flow, 4 AI-ready habits | [Week 2 Guide](docs/week-02-agile-teams/README.md) · [Git Guide](docs/week-02-agile-teams/git-vscode-guide.md) | [Completed (Story 2.1)](assignments/week-02/submission.md) |
| **03** | **Python 3 Foundations — Giving the AI "Hands"** | Build structured dictionary/JSON outputs, `is_nan`, `safe_eval_price`, and the eCOMMart Mini Agent Tool | [Week 3 Guide](docs/week-03-python-fundamentals/README.md) · [Worked Examples](docs/week-03-python-fundamentals/04%20-%20Worked%20Examples/worked_examples.md) | [12 Exercises & Solutions](assignments/week-03/README.md) |
| **04** | **Python OOP — Organizing the Mess** | Build `ProductCatalog` class reading JSON inventory & handling file errors | *Upcoming* | *Pending* |
| **05** | **Databases — Giving the AI "Memory"** | Migrate from flat files to persistent SQLite storage for orders & inventory | *Upcoming* | *Pending* |
| **06** | **Pro Code — Testing & Environments** | Virtual environments (`venv`), `.env` secret security, and `pytest` suites for agent tools | *Upcoming* | *Pending* |

*(See [curriculum/roadmap-24-weeks.md](curriculum/roadmap-24-weeks.md) and [curriculum/shared-resources.md](curriculum/shared-resources.md) for all official links).*

---

## Official Shared Resource Links

| Week | Resource Type | Official Link |
| :---: | :--- | :--- |
| **Week 1** | Storyline Doc · Canva Board · Slides | [Google Doc](https://docs.google.com/document/d/1zcseX_Y3L6AhCB3RTdyJg1fUe-XUQFQtMIhkg2nSR6o/edit?tab=t.0) · [Canva Board](https://www.canva.com/design/DAHXI3TXQf0/RLkq3ACk8xdsi7tN3J6n6A/edit) · [Google Slides](https://docs.google.com/presentation/d/1P5tT_zEwMmrhfRLjK5oco8Jt60uy70m4/edit?slide=id.p29#slide=id.p29) |
| **Week 2** | Slides · Hands-On Guide · GitHub | [Google Slides](https://docs.google.com/presentation/d/1X3-hC88pISr2zKGAqcNN9cEKqs_Ny0PT/edit?usp=sharing&ouid=106370953992675903899&rtpof=true&sd=true) · [Hands-On Doc](https://docs.google.com/document/d/1wJbBtZ0uD2mYNdpKZgM3i-vDH6-M3t8YdhWp9ElofZA/edit?usp=sharing) · [GitHub](https://github.com/) |
| **Week 3** | Python Fundamentals Shared Drive | [Google Drive Folder](https://drive.google.com/drive/folders/1UbHs_5Bv4EknTtKenINPyHCuyilTwhMn?usp=sharing) |

---

## Quick Start: Running the eComMART Agent Tools

```bash
# Run Week 2 Seller Agent Floor-Price Negotiation Tool
python3 projects/seller-agent/counter_offer.py

# Run Week 3 eCOMMart Mini Agent Order & Delivery Tool
python3 projects/seller-agent/mini_agent_tool.py
```
