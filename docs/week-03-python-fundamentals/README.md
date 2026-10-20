# Week 3: Python 3 Foundations — Giving the AI "Hands"

> **Module:** Week 3 — Python Fundamentals (`eCOMMart AI Squad`)  
> **Narrative Milestone:** Before an AI agent can check inventory, calculate discounts, or process an order, it needs deterministic Python functions ("hands") that accept inputs, validate edge cases (`is_nan`, `try/except`), and return structured Dictionaries/JSON.  
> **Official Shared Drive:** [Week 3 Google Drive Folder](https://drive.google.com/drive/folders/1UbHs_5Bv4EknTtKenINPyHCuyilTwhMn?usp=sharing)  

---

## Course Structure

```text
docs/week-03-python-fundamentals/
├── README.md                                 # Week 3 Master Index & Learning Path
├── img/                                      # Course Diagrams & Visual Illustrations
├── 01 - Introduction to Python/              # Lessons 001 – 005
├── 02 - Variables, Literals and Constants/   # Lessons 006 – 009
├── 03 - Programming Building Blocks/
│   ├── A - Operators and Conditions/         # Lessons 010 – 013
│   ├── B - Loops/                            # Lesson 014
│   ├── C - Functions and Scope/              # Lessons 015 – 019
│   └── D - Collections/                      # Lessons 020 – 025
├── 04 - Worked Examples/
│   └── worked_examples.md                    # 6 Complete eCOMMart Programs (up to Mini Agent Tool)
└── 05 - Exercises/
    ├── exercises.md                          # 12 Graded Exercises (Beginner to Capstone)
    └── solutions.md                          # Reference Solutions
```

---

## Learning Path (Follow in Order)

### 01 — Introduction to Python
| Lesson File | What You Will Learn |
| :--- | :--- |
| [`001_What_is_Programming.md`](01%20-%20Introduction%20to%20Python/001_What_is_Programming.md) | What programming is, interpreters vs. compilers, and why Python |
| [`002_Python_Programming.md`](01%20-%20Introduction%20to%20Python/002_Python_Programming.md) | Key features and industry uses of Python in AI & backends |
| [`003_How_to_Install_Python.md`](01%20-%20Introduction%20to%20Python/003_How_to_Install_Python.md) | Setting up Python and VS Code |
| [`004_Hello_World.md`](01%20-%20Introduction%20to%20Python/004_Hello_World.md) | Writing and running your first Python program and indentation rules |
| [`005_Python_Keywords_and_Identifiers.md`](01%20-%20Introduction%20to%20Python/005_Python_Keywords_and_Identifiers.md) | Reserved keywords and identifier naming rules |

### 02 — Variables, Literals and Constants
| Lesson File | What You Will Learn |
| :--- | :--- |
| [`006_Python_Variables_and_Constants.md`](02%20-%20Variables,%20Literals%20and%20Constants/006_Python_Variables_and_Constants.md) | Storing and naming data in memory |
| [`007_Python_Literals.md`](02%20-%20Variables,%20Literals%20and%20Constants/007_Python_Literals.md) | Fixed values: numbers, single/double/triple-quoted strings, booleans |
| [`008_Data_Types_and_Type_Conversion.md`](02%20-%20Variables,%20Literals%20and%20Constants/008_Data_Types_and_Type_Conversion.md) | Core data types, `None`, `NaN`, and explicit type conversion |
| [`009_Date_and_Time.md`](02%20-%20Variables,%20Literals%20and%20Constants/009_Date_and_Time.md) | Working with dates, timestamps, and `datetime` |

### 03 — Programming Building Blocks

#### A — Operators and Conditions
| Lesson File | What You Will Learn |
| :--- | :--- |
| [`010_Python_Operators.md`](03%20-%20Programming%20Building%20Blocks/A%20-%20Operators%20and%20Conditions/010_Python_Operators.md) | Arithmetic, comparison, assignment, and logical operators |
| [`011_If_elif_else.md`](03%20-%20Programming%20Building%20Blocks/A%20-%20Operators%20and%20Conditions/011_If_elif_else.md) | Decision-making and branching logic (`if / elif / else`) |
| [`012_Conditional_Statements.md`](03%20-%20Programming%20Building%20Blocks/A%20-%20Operators%20and%20Conditions/012_Conditional_Statements.md) | `for` loops, `range()`, `break`, `continue`, and `pass` |
| [`013_List_Comprehensions.md`](03%20-%20Programming%20Building%20Blocks/A%20-%20Operators%20and%20Conditions/013_List_Comprehensions.md) | Concise comprehensions for filtering and transforming lists |

#### B — Loops
| Lesson File | What You Will Learn |
| :--- | :--- |
| [`014_While_Loops_and_User_Input.md`](03%20-%20Programming%20Building%20Blocks/B%20-%20Loops/014_While_Loops_and_User_Input.md) | `while` loops and interactive CLI programs with `input()` |

#### C — Functions and Scope
| Lesson File | What You Will Learn |
| :--- | :--- |
| [`015_Functions.md`](03%20-%20Programming%20Building%20Blocks/C%20-%20Functions%20and%20Scope/015_Functions.md) | Defining and calling reusable functions with docstrings |
| [`016_More_Functions.md`](03%20-%20Programming%20Building%20Blocks/C%20-%20Functions%20and%20Scope/016_More_Functions.md) | Default parameters, keyword arguments, and return contracts |
| [`017_Args_and_Kwargs.md`](03%20-%20Programming%20Building%20Blocks/C%20-%20Functions%20and%20Scope/017_Args_and_Kwargs.md) | Flexible argument handling (`*args` and `**kwargs`) |
| [`018_Nested_Statements_and_Scope.md`](03%20-%20Programming%20Building%20Blocks/C%20-%20Functions%20and%20Scope/018_Nested_Statements_and_Scope.md) | Variable scope and the **LEGB** (`Local → Enclosing → Global → Built-in`) rule |
| [`019_Exceptions.md`](03%20-%20Programming%20Building%20Blocks/C%20-%20Functions%20and%20Scope/019_Exceptions.md) | Graceful error handling (`try / except / else / finally` and `raise`) |

#### D — Collections
| Lesson File | What You Will Learn |
| :--- | :--- |
| [`020_Lists.md`](03%20-%20Programming%20Building%20Blocks/D%20-%20Collections/020_Lists.md) | Ordered, mutable sequences (`list`) |
| [`021_Advanced_Lists.md`](03%20-%20Programming%20Building%20Blocks/D%20-%20Collections/021_Advanced_Lists.md) | List methods, slicing, sorting, and nested lists |
| [`022_Dictionaries.md`](03%20-%20Programming%20Building%20Blocks/D%20-%20Collections/022_Dictionaries.md) | Key-value mappings (`dict`) — the primary data structure for AI Agent Tool I/O |
| [`023_Tuples.md`](03%20-%20Programming%20Building%20Blocks/D%20-%20Collections/023_Tuples.md) | Immutable, ordered records (`tuple`) and unpacking |
| [`024_Sets_and_Booleans.md`](03%20-%20Programming%20Building%20Blocks/D%20-%20Collections/024_Sets_and_Booleans.md) | Unique collections (`set`) and boolean truthiness |
| [`025_Advanced_Sets.md`](03%20-%20Programming%20Building%20Blocks/D%20-%20Collections/025_Advanced_Sets.md) | Set operations: union, intersection, difference, and symmetric difference |

---

## Worked Examples & Practice

- **[04 — Worked Examples](04%20-%20Worked%20Examples/worked_examples.md):** 6 complete runnable eCOMMart programs culminating in **Example 6: The eCOMMart Mini Agent Tool** (runnable at [`projects/seller-agent/mini_agent_tool.py`](../../projects/seller-agent/mini_agent_tool.py)).
- **[05 — Exercises](../../assignments/week-03/exercises.md):** 12 graded exercises from Beginner (`🟢`) to Advanced (`🔴`), culminating in **Exercise 12: Capstone eCOMMart Order Terminal**.
- **[Reference Solutions](../../assignments/week-03/solutions.md):** Full reference implementations for all 12 exercises.
- **[Live Session Demos (`Cohort 1 - demo`)](../../labs/week-03-python-fundamentals/cohort-1-demo/):** Live scripts (`001.py`–`004.py`) demonstrating variables, user input, discount tiers, and loops.
