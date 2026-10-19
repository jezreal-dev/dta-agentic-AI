# 24-Week Curriculum & Narrative Roadmap

> **Program:** Agentic AI in Software Development Academy (Oct – Mar)  
> **Overarching Scenario:** The **eComMART AI Engineering Squad**  

---

## Why Agile for Agentic AI? (The Industry Challenge)

In traditional software projects (**Waterfall**), teams receive a fixed set of requirements, spend months writing a massive specification, write the code, and deploy it. When enterprises tried building AI systems this way, it failed:
- AI models are probabilistic and can hallucinate.
- Real-world marketplace data is messy and unpredictable.
- A rigid upfront plan becomes obsolete on day one of testing.

**The Industry Solution:** Build AI iteratively in short **Sprints** (1–4 weeks). Combine Scrum's planning rhythm with an AI-specific loop:
$$\text{Experiment} \longrightarrow \text{Evaluate} \longrightarrow \text{Improve}$$

---

## Phase 1: Building the Engine (Weeks 1 – 6)

In the first 6 weeks on the eComMART AI Squad, no LLM is connected yet. An AI agent is just a brain—without deterministic tools ("hands"), persistent storage ("memory"), and strict guardrails ("rules"), it cannot safely operate a B2B marketplace.

### Week 1: Agile Fundamentals & Welcome to the Team
- **The Story:** It is week one at eComMART. Leadership arrives with a vague idea: *"I want an AI that qualifies our leads and negotiates for our suppliers."*
- **Demo Focus:** Turning a messy idea into Agile **Epics**, breaking them into **User Stories** using the **SMART** criteria (*Specific, Measurable, Achievable, Relevant, Time-bound*), and separating **Functional Requirements (FR)** from **Non-Functional Requirements (NFR)** such as latency and hallucination limits.
- **Topics Covered:**
  - Agile mindset and principles; Waterfall vs. iterative delivery.
  - Scrum and Kanban overview.
  - Core Agile Workflow: `Epic → User Story → Task`.
  - Applying SMART and INVEST criteria to User Stories and Acceptance Criteria.
  - Product and Sprint Backlogs; Sprint Planning, Review, and Retrospective.
  - Acceptance Criteria (`Given / When / Then`) vs. Definition of Done (`DoD`).
  - Agile Transformation: Product-oriented vs. project-oriented delivery, cross-functional teams.
  - Agile for AI Projects: `Experiment → Evaluate → Improve`; handling uncertain requirements; MVP vs. production-ready solution.

### Week 2: Working on a Real Dev Team (Serving in Agile Teams + Collaboration)
- **The Story:** Day 1 of Sprint 1. Two engineers push untested code with conflicting assumptions directly to `main`, causing the Seller Agent to counter offers at \$65 on an \$80 floor price.
- **Demo Focus:** Running a real Sprint. Taking a User Story from Week 1, slicing it into small role-tagged tasks (`DEV`, `DATA`, `EVAL`, `QA`, `UX`, `SEC`), checking coverage against Acceptance Criteria, and enforcing a clean Git branch + Pull Request + Code Review workflow.
- **Topics Covered:**
  - Working in Agile Teams: The 3 Scrum roles (`Product Owner`, `Scrum Master`, `Developers`), shared ownership, cross-functional collaboration.
  - Agile Team Practices: Backlog Refinement, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective.
  - Effective Collaboration: Slicing stories into tasks, coverage testing (build + proof), managing dependencies and blockers, specific/kind/actionable feedback.
  - Git & Collaboration: Repositories, branches, commits, Pull Requests, code review checklists, merge conflict resolution.
  - Preparing Teams for AI Delivery: The 4 AI-ready habits (Run experiments, Log failure cases, Measurable success criteria, Human in the loop).

### Week 3: Python 3 Foundations — Giving the AI "Hands"
- **The Story:** Before an AI can "check order status" or "counter an offer," we need deterministic Python functions that execute the business logic and return structured data.
- **Demo Focus:** Writing Python scripts that categorize inputs and output structured Dictionaries/JSON—the exact data structures LLMs use for tool calling.
- **Topics Covered:**
  - Python Basics: Variables and data types (`str`, `int`, `float`, `bool`, `None`).
  - Python Collections: Lists, Tuples, Dictionaries, Sets.
  - Why dictionaries and JSON-style structures matter for AI applications.
  - Programming Logic: `if/elif/else`, `for` and `while` loops, basic exception handling (`try/except`).
  - Functions: Parameters, return values, modular reusable functions as the foundation for future **Agent Tools**.

### Week 4: Python OOP — Organizing the Mess
- **The Story:** As our scripts grow, unstructured spaghetti code becomes fragile and impossible for an AI framework to maintain.
- **Demo Focus:** Transitioning to Object-Oriented Programming (OOP) by building a `ProductCatalog` class that loads and queries a JSON file of eComMART inventory.
- **Topics Covered:**
  - Object-Oriented Python: Classes and objects, attributes and methods, `__init__`, encapsulation, and composition.
  - Why OOP Matters for AI Applications: Structuring tools, services, and state; understanding class-based AI SDKs (such as LangChain and Bedrock agents).
  - File Handling: Reading, writing, and appending with `with open()`; text files, JSON, and CSV.
  - Configuration & Data: Loading configuration from JSON, saving application output, and gracefully handling file/parsing errors.

### Week 5: Databases — Giving the AI "Memory"
- **The Story:** Flat text files are slow and easily corrupted under concurrent access. If our Buyer Agent negotiates a quote or submits an RFQ, the system must remember it permanently. An AI without a database has amnesia.
- **Demo Focus:** Moving from flat JSON files to a relational **SQLite** database, writing Python functions to insert, query, and update eComMART orders, RFQs, and inventory.
- **Topics Covered:**
  - Database Fundamentals: Tables, rows, columns, primary keys, and persistent storage.
  - Essential SQL: `INSERT`, `SELECT`, `UPDATE`, `DELETE`.
  - Python Database Integration: `sqlite3` connections and cursors, parameterized queries (preventing SQL injection), transactions (`commit`), and exception handling.
  - Preparing for Agentic AI: Persistent state, execution history, audit logs (NFR-06), and long-term agent memory.

### Week 6: Pro Code — Testing & Environments
- **The Story:** Next phase, we connect real AI models. If an autonomous agent misfires, it could corrupt inventory or leak API credentials. We need professional engineering safety nets.
- **Demo Focus:** Isolating project dependencies with Python Virtual Environments (`venv`), protecting credentials with `.env` files, and writing automated `pytest` test suites.
- **Topics Covered:**
  - Python Virtual Environments: Creating and activating `venv`, managing packages with `pip`.
  - Dependency & Configuration Management: `requirements.txt`, pinning versions, environment variables, `.env`, and keeping API keys out of Git (`SEC`).
  - Organizing Python Applications: Modules, packages, imports, separating business logic, config, database, and tests.
  - Testing Fundamentals: Automated testing with `pytest`, `Arrange → Act → Assert`, testing edge cases and error scenarios (`QA` & `EVAL`).
  - Preparing for Agentic AI Development: Testing deterministic agent tools thoroughly before handing control to an LLM.

---

## Phases 2 – 4: Agentic AI Engineering (Weeks 7 – 24 Overview)

| Phase | Weeks | Focus Area | Key Technologies & Deliverables |
| :--- | :---: | :--- | :--- |
| **Phase 2: LLM Foundations & Tool Use** | 07 – 12 | Connecting LLMs to deterministic Python tools, structured outputs, prompt engineering, and evaluation harnesses | Prompt templates, tool schemas, failure-case regression suites, latency & hallucination benchmarking |
| **Phase 3: AWS Bedrock & Claude Agents** | 13 – 18 | Enterprise cloud AI with AWS Bedrock, Claude model family, Knowledge Bases (RAG), and Bedrock Guardrails | AWS Bedrock SDK (`boto3`), Claude tool calling, supplier catalog RAG, floor-price & safety guardrails |
| **Phase 4: Multi-Agent Commerce System** | 19 – 24 | End-to-end orchestration of the **Buyer Agent** and **Seller Agent**, human-in-the-loop workflows, and Capstone delivery | Multi-agent RFQ & negotiation pipeline, full observability, audit trails, and live stakeholder Sprint Review |
