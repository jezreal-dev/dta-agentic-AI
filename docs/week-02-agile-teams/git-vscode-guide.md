# Week 2: Git, GitHub & VS Code Collaboration Guide

> **Companion to:** [Week 2: Serving in Agile Teams](README.md)  
> **Code Implementation:** [`projects/seller-agent/counter_offer.py`](../../projects/seller-agent/counter_offer.py)  

---

## Part 0: Key Concepts Before We Start

Why do engineering squads use Git?
Imagine Muhammad saves `counter_offer.py` at 3:00 PM. Abdullah saves his version at 4:00 PM over the same file. Without version control, Muhammad's floor-price logic is silently erased.

| Concept | What It Means | eComMART Squad Purpose |
| :--- | :--- | :--- |
| **Repository (Repo)** | The project folder tracked by Git (local and on GitHub) | Single source of truth for the squad's code and docs |
| **Commit** | A saved snapshot of changes with author, timestamp, and message | Full history—you can always inspect or roll back to any checkpoint |
| **Branch** | An isolated workspace (`feature/story-2-2-stock-check`) | Lets you build and test a feature without risking `main` |
| **Pull Request (PR)** | A formal request to merge your branch into `main` | Opens a space for teammates to review code before it goes live |
| **Merge** | Combining an approved branch into `main` | Delivers verified, reviewed increments to the shared codebase |

---

## Part 1 – 4: One-Time Environment Setup

### 1. Verify Git Installation
```bash
git --version
```
*(Should display `git version 2.x.x`).*

### 2. Configure Your Git Identity
Every commit carries your name and GitHub email:
```bash
git config --global user.name "Jezreal Momoh"
git config --global user.email "jezreelmomoh1234@gmail.com"
```
Verify configuration:
```bash
git config --global user.name
git config --global user.email
```

### 3. VS Code & GitHub Integration
- Open the integrated terminal in VS Code with `` Ctrl + ` ``.
- Install the **GitHub Pull Requests** extension from the VS Code Extensions panel.
- Sign in to GitHub via the **Accounts** icon in the bottom-left sidebar.

---

## Part 5 – 6: First Commit (`counter_offer.py` — Baseline)

### Scenario
You are building the initial negotiation function for **Story 2.2** (*Counter low offers automatically*), enforcing `NFR-03` (never counter below the supplier's floor price).

```python
# counter_offer.py
# Story 2.2 - Counter low offers automatically

def counter_offer(listed_price, buyer_offer, floor_price):
    """
    Returns a counter-offer or flags the request for review.

    listed_price : the original price on the catalog
    buyer_offer  : the price the buyer is proposing
    floor_price  : the minimum price the supplier accepts
    """
    if buyer_offer >= listed_price:
        # Buyer paid full price - accept immediately
        return {"action": "accept", "price": buyer_offer}

    if buyer_offer < floor_price:
        # Below the minimum - counter at the floor (enforces NFR-03)
        return {"action": "counter", "price": floor_price}

    # Between floor and listed price - counter at the midpoint
    mid = (listed_price + buyer_offer) / 2
    return {"action": "counter", "price": round(mid, 2)}


# Quick test
if __name__ == "__main__":
    result = counter_offer(100, 85, 80)
    print(f"Test 1: {result}")   # expect counter at 92.5

    result = counter_offer(100, 70, 80)
    print(f"Test 2: {result}")   # expect counter at 80.0

    result = counter_offer(100, 100, 80)
    print(f"Test 3: {result}")   # expect accept
```

### Commit Message Standards
A commit message must state **what changed and why** in plain English:

| Commit Message | Verdict | Reason |
| :--- | :---: | :--- |
| `git commit -m "fix stuff"` | ❌ Bad | Vague; gives teammates zero context |
| `git commit -m "changes"` | ❌ Bad | Does not explain what was changed or why |
| `git commit -m "Add counter_offer with floor price check"` | ✅ Good | Clear, specific, describes the exact capability added |
| `git commit -m "Add stock=0 check - fixes AC-3 (no invented availability)"` | ✅ Good | Links the code change directly to Story Acceptance Criteria |

---

## Part 7: Feature Branches and Pull Requests

> **Golden Rule:** Never commit directly to `main` during feature development. Always follow:  
> `branch → work → test → commit → push → Pull Request → review → merge`

### 7.1 Create a Feature Branch
Naming convention: `feature/<story-id>-<short-description>`

```bash
git checkout main
git pull
git checkout -b feature/story-2-2-stock-check
```

### 7.2 Add Out-of-Stock Protection (`AC-3` / `NFR-02`)
Update `counter_offer.py` so the Seller Agent never invents availability when `stock == 0`:

```python
def counter_offer(listed_price, buyer_offer, floor_price, stock=None):
    """
    Returns a counter-offer or flags the request for review.
    stock : number of units available (None means unknown)
    """
    # AC-3: do not invent availability
    if stock is not None and stock <= 0:
        return {"action": "unavailable", "reason": "out of stock"}

    if buyer_offer >= listed_price:
        return {"action": "accept", "price": buyer_offer}

    if buyer_offer < floor_price:
        return {"action": "counter", "price": floor_price}

    mid = (listed_price + buyer_offer) / 2
    return {"action": "counter", "price": round(mid, 2)}
```

Add `Test 4` to verify out-of-stock handling:
```python
    # Test 4: out of stock
    result = counter_offer(100, 85, 80, stock=0)
    print(f"Test 4: {result}")   # expect unavailable
```

Stage, commit, and push the branch:
```bash
git add counter_offer.py
git commit -m "Add stock=0 check - fixes AC-3 (no invented availability)"
git push -u origin feature/story-2-2-stock-check
```

### 7.3 Pull Request Description Template
When opening a Pull Request on GitHub, use this structured template:

```markdown
## What this changes
Adds `stock=0` check to `counter_offer` so the agent never invents availability for out-of-stock items.

## Story
Story 2.2 - AC-3: no invented availability

## How I tested
- Test 4: `counter_offer(100, 85, 80, stock=0)` returns `{"action": "unavailable", "reason": "out of stock"}`
- Existing tests 1, 2, 3 still pass

## Please check
- Does the `stock=None` default keep old calls working?
- Is the reason message clear enough for the supplier?
```

---

## Part 8: Code Review Checklist & Merging

When reviewing a teammate's Pull Request, evaluate against these five questions:

| Reviewer Checklist Item | What to Look For |
| :--- | :--- |
| **1. Does it satisfy the story & ACs?** | `AC-3` requires no invented availability—does the `stock == 0` check enforce that? |
| **2. Are there automated tests?** | Was `Test 4` added, and do all existing tests (`Test 1`–`3`) still pass? |
| **3. Are variable & action names clear?** | Are `"unavailable"` and `"out of stock"` clear to a supplier reading the audit log? |
| **4. Any secrets or hard-coded credentials?** | Confirm no passwords, tokens, or API keys appear in the diff (`SEC`). |
| **5. Is the diff small and focused?** | Small enough to review thoroughly in a single sitting. |

After approval and merging on GitHub, delete the remote feature branch and sync your local `main`:
```bash
git checkout main
git pull
```

---

## Part 9: Quick Git Command Reference

| Command | Description |
| :--- | :--- |
| `git --version` | Check that Git is installed |
| `git config --global user.name "Name"` | Set your name for commits |
| `git config --global user.email "you@email.com"` | Set your email for commits |
| `git clone <URL>` | Download a repository from GitHub to your computer |
| `git status` | Show modified and untracked files |
| `git add <filename>` | Stage a specific file for commit |
| `git add .` | Stage all changed files |
| `git commit -m "message"` | Record a snapshot with a descriptive message |
| `git push` | Upload local commits to GitHub |
| `git pull` | Download and merge the latest changes from GitHub |
| `git pull --rebase` | Pull remote commits and replay your local commits cleanly on top |
| `git checkout main` | Switch to the `main` branch |
| `git checkout -b feature/my-branch` | Create a new branch and switch to it immediately |
| `git branch` | List local branches (`*` indicates current branch) |
| `git log --oneline` | View compact commit history |
| `git diff` | Inspect unstaged line-by-line changes |

---

## Part 10: Troubleshooting Common Git Issues

1. **`Failed to push: rejected`:**
   - *Cause:* Remote GitHub has commits that your local clone does not have yet.
   - *Fix:* Run `git pull --rebase`, resolve any conflicts if prompted, and then run `git push`.
2. **Merge Conflicts (`<<<<<<< HEAD` / `=======` / `>>>>>>>`):**
   - *Cause:* Two people edited the exact same lines of a file.
   - *Fix:* Inspect both blocks (`HEAD` is your current branch; the bottom block is incoming), keep the correct combined logic, remove the `<<<`, `===`, `>>>` markers, save, stage (`git add`), and commit.
3. **`Please tell me who you are`:**
   - *Cause:* `user.name` or `user.email` has not been set in Git config.
   - *Fix:* Run the `git config --global` commands from Part 1.
