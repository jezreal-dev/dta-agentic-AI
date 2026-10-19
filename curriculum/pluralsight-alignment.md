# Pluralsight Learning Channel & DTA Dashboard Alignment

> **Pluralsight Channel:** [Agentic AI in Software Development Academy | Oct - Mar Learning Channel](https://app.pluralsight.com/channels/details/ef7cfa5a-4fd4-41d7-99f4-44aada048e1f)  
> **DTA Learner Portal:** [Digital Training Academy Dashboard](https://dta.education.gov.ng/learners/dashboard)  
> **Channel Curator:** Emilie Jones  
> **Assigned DTA Mentor:** Ogiugo Mike  

---

## Overview

The **Agentic AI in Software Development Academy** blends two complementary learning modes:
1. **Live Weekly Instructor-Led Sessions (Every Tuesday):** Applied case studies with the **eComMART AI Engineering Squad**, live coding demos, breakout activities, and weekly takeaway assignments.
2. **Self-Paced Pluralsight Modules:** Assigned weekly on the Pluralsight Learning Channel to build deep conceptual and technical mastery ahead of and following each live Tuesday session.

---

## Assigned Courses & Curriculum Mapping

| Pluralsight / DTA Module | Aligned Academy Week(s) | Core Competencies Covered | eComMART Squad Application | Status |
| :--- | :---: | :--- | :--- | :---: |
| **Agile Transformation: Organizational Agility** | Week 1 | Agile mindset, iterative vs. Waterfall delivery, product-oriented teams, continuous feedback loops | Framing eComMART's AI transformation into Epics (`E1`–`E3`) and an MVP Sprint 1 backlog | Assigned / In Progress |
| **Serving in Agile Teams** | Week 2 | Scrum roles (`PO`, `SM`, `Developers`), Sprint ceremonies, slicing stories into tasks, WIP limits, shared ownership | Running Sprint 1 for Story 1.1 & Story 2.2, role-tagging tasks (`DEV`, `DATA`, `EVAL`, `QA`, `UX`, `SEC`), and PR code reviews | In Progress (~31.5%) |
| **Python 3: The Big Picture** | Week 3 | Python's ecosystem, philosophy, use cases in automation, data processing, and AI application backends | Understanding how Python glue code connects data layers (`ProductCatalog`) with LLM tool calls | Assigned |
| **Python 3 Fundamentals** | Weeks 3 – 6 | Data types, collections (`dict`, `list`), control flow, functions, OOP classes, file I/O, and unit testing | Building `check_stock()`, `counter_offer()`, BANT lead scoring, `ProductCatalog`, and SQLite persistence | Assigned |
| **AWS Bedrock & Claude Agent Development** *(Upcoming Additions)* | Weeks 7 – 24 | Foundation models on AWS Bedrock, Anthropic Claude prompting, tool use, RAG knowledge bases, and multi-agent guardrails | Connecting the **Seller Agent** and **Buyer Agent** to Claude on AWS Bedrock with deterministic guardrails | Upcoming |

---

## Weekly Study Cadence

To maximize retention and stay ahead on both the DTA Dashboard and Pluralsight Channel:

1. **Before Tuesday Live Class:**
   - Complete the assigned Pluralsight video modules for the week.
   - Log key takeaways in [`notes/pluralsight/`](../notes/pluralsight/README.md).
2. **During Tuesday Live Class:**
   - Capture live demo notes and breakout room solutions in [`notes/tuesday-sessions/`](../notes/tuesday-sessions/README.md).
   - Start the weekly Takeaway Hands-on Exercise during the final 15 minutes of class.
3. **After Tuesday Live Class (Wednesday – Monday):**
   - Complete and commit the weekly assignment inside [`assignments/`](../assignments/).
   - Practice the code examples inside [`labs/`](../labs/) and [`projects/`](../projects/) using a feature branch and Pull Request workflow.
