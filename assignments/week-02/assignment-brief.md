# Week 2 Takeaway Hands-On Exercise: Mini Sprint Plan

> **Source:** Week 2 Participant Guide — Part 7: Takeaway Hands-on Exercise  
> **Estimated Time:** 60 to 90 minutes  
> **Completed Submission:** [`submission.md` (Story 2.1 — Score Leads with BANT)](submission.md)  
> **Blank Template:** [`template.md`](template.md)  

---

## Your Task

Create a **Mini Sprint Plan** for **one AI-related user story**, covering tasks, risks, acceptance criteria, and a Definition of Done. Work on your own, at your own pace.

### What You Will Produce
A one- or two-page plan for a single story.
- **Eligible Stories:** Choose one of the five stories you wrote in Week 1, or pick from the eComMART backlog:
  - **Story 2.1:** *Score leads with BANT* (`Epic E2`, 5 pts) — **[Selected for Submission]**
  - **Story 3.1:** *Submit an RFQ in one step* (`Epic E3`, 5 pts)
  - **Story 3.2:** *Check RFQ status* (`Epic E3`, 3 pts)
- **Excluded Stories:** Do **not** choose Story 1.1, Story 2.2, or Story 2.3, because they have already been planned or practised in class.

---

## Required Steps

1. **Restate the Story:** Write the story in the `"As a... I want... so that..."` form, and state which Epic (`E1`, `E2`, or `E3`) and Story Point size it belongs to.
2. **Sprint Goal:** Write a clear Sprint Goal in **one sentence**.
3. **Acceptance Criteria:** Write **3 to 5 acceptance criteria** in `Given / When / Then` form. Include **at least one that is measurable** (a number, a threshold, or a count of test runs).
4. **Task Breakdown & Coverage Test:** Break the story into **4 to 8 tasks**. Give each one a role tag (`DEV`, `DATA`, `EVAL`, `QA`, `UX`, `SEC`) and a size. Run the **coverage test**: *does every criterion have a task that builds it and one that proves it?*
5. **Dependencies & Blockers:** List dependencies and blockers you can foresee, and explain how you will reduce each.
6. **Risks:** Name **at least 3 risks**, with **at least one specific to AI behaviour**, and a mitigation for each.
7. **Expected Failure Cases:** List **2 or 3 expected failure cases** that you would put in the failure case log.
8. **Human Validation (Human-in-the-Loop):** State where a human steps in (**Before**, **During**, and **After** the AI acts).
9. **Definition of Done:** Write the Definition of Done checklist for this story, including at least one story-specific item.

---

## Worked Fragment Example (from Participant Guide — Story 3.2)

| Section | Example Content |
| :--- | :--- |
| **Story** | As a buyer, I want to check my RFQ status, so I do not have to chase suppliers. (`3 pts`, `Epic E3`) |
| **Sprint Goal** | A buyer can see where their RFQ stands without contacting anyone. |
| **AC-1** | **Given** a submitted RFQ, **when** the buyer checks its status, **then** the current status is shown. |
| **AC-2 (Measurable)** | **Given** 20 test requests, **when** status is checked, **then** 95% of replies arrive within 5 s. |
| **Task Example 1** | `[DEV]` Write `get_rfq_status(rfq_id)`, covers `AC-1`. |
| **Task Example 2** | `[QA]` Test an unknown RFQ ID returns a clear message, covers `AC-1`. |
| **AI-Specific Risk** | The agent could invent a status for an RFQ that does not exist. *Mitigation:* Read status only from stored data, and test with unknown IDs. |

---

## Self-Check Rubric Before Finishing

| Check | What Good Looks Like |
| :--- | :--- |
| **Story is clear** | A teammate could explain the business value in one sentence |
| **Criteria are testable** | Each one is clearly pass or fail, and at least one has a measurable number |
| **Tasks are small** | Each can be finished in 1–2 days, with one owner and one role tag |
| **Coverage verified** | Every criterion has both a **build task** and a **proof task** |
| **Dependencies visible** | You named what must exist first and how to reduce waiting |
| **AI risk included** | At least one risk specifically addresses AI hallucination, drift, or bad input |
| **Failure log seeded** | 2–3 concrete input/expected/failure rows ready to become regression tests |
| **Human-in-the-loop defined** | Clear human roles *Before*, *During*, and *After* the agent acts |
