# Repo Tree — Structure & Change Impact

Full tree of the repository. Each entry says what it is; the "Change impact" section at the bottom says **what else must be updated** whenever something here changes.

## Tree

```text
Python_Programming_Lab/
│
├── README.md                 # Landing page — lab overview table, getting started
│                              ⚠ any lab/file change → also listed here
├── LICENSE.md                # License statement (no other file depends on it)
├── CONTRIBUTING.md           # How to contribute / add programs
├── TREE.md                   # ← this file (mirror of the repo; keep in sync)
├── .gitignore                # Ignore __pycache__, .venv, editor/OS files
│
├── setupgit.md               # Personal notes: git setup steps (standalone)
├── pythonsetup.md            # Personal notes: Python install steps (standalone)
│
├── public/
│   ├── suiit-logo.png            College logo, white variant — README.md,
│   │                             dark mode (invisible on light theme)
│   ├── suiit-logo-color.png      College logo, coloured variant — README.md
│   │                             light mode
│   └── python-logo.png           Python mark — README.md header (right),
│                                 from Wikimedia (Python-logo-notext)
│
├── lab1/
│   └── assignment1.py            Basics of print() — patterns, newline handling
│
├── lab2/
│   ├── assignment2.py            Lab 2 graded work: variables, data types, scope
│   ├── labactivity1.py           Assignment & dynamic typing
│   ├── labactivity2.py           Local & global scope
│   ├── labactivity3.py           input() and print() parameters
│   ├── Lab2.docx                 Lab 2 documentation (open in Word)
│   └── test.py                   Scratch file — f-string testing
│
├── lab3/
│   ├── program01.py … 09.py      Input, arithmetic ops, area/perimeter, SI,
│   │                             temperature, map() — need input() prompts
│   ├── program10.py … 20.py      Formatted output: sep, end, \n, \t,
│   │                             precision, repr(), tables
│   ├── program21.py … 35.py      Variables, operators, swapping, data types
│   └── program36.py … 45.py      Applications: gross salary, currency, BMI,
│                                 bills, reports
│
├── lab4/
│   ├── arithmetic.py             + - * / // % **
│   ├── relational.py             > < >= <= == !=
│   ├── logical.py                and, or, not
│   ├── bitwise.py                & | ^ ~ << >>
│   ├── assignment.py             = += -= *= /= //= %= **=
│   ├── membership_identity.py    in, not in, is, is not
│   └── ternary.py                value_if_true if condition else value_if_false
│
├── lab5/
│   ├── datatypes.md              Theory notes for every data type
│   ├── integer.py                int: + - // % **, bin/oct/hex, int('42')
│   ├── float.py                  float: decimals, scientific notation, rounding
│   ├── complex.py                complex: real/imag, abs(), conjugate, ** 2
│   ├── string.py                 str: index, slice, methods, f-strings
│   ├── classwork1.py             str ops on "Hello Suiit": slicing, case,
│   │                             search, strip/replace/join, f-string
│   ├── boolean.py                bool: truthiness, and/or/not
│   ├── list.py                   list: append/insert/remove/pop, sort
│   ├── tuple.py                  tuple: immutable, count/index, unpacking
│   ├── set.py                    set: unique elements, | & - ^
│   ├── dictionary.py             dict: key→value, get/del, items()
│   └── frozenset.py              frozenset: immutable set
│
└── lab6/
    ├── strings.md                Theory notes: indexing, slicing, methods,
    │                             split/join, immutability
    ├── string.py                 String operations demo — expression indices
    │                             (s[1+5]), case, search, strip, split/join,
    │                             f-string, TypeError on s[0] = "R"
    └── string_operators.py       String operators: + * in % comparison,
                                  += rebuild (original unchanged)
```

## Change impact — when you edit here … update there

| You change / add… | Must also update |
|---|---|
| **A program file** (fix a bug, add a demo) in any lab | Its own file only, **plus the matching line in [`README.md`](README.md)** (lab table row / structure) — README describes one entry per file-group |
| **A new file** in an existing lab folder | `README.md` structure section → or reference [this tree](TREE.md); and the lab's overview-table row if the contents changed materially |
| **A new lab folder** `labN/` | `README.md`: new row in Labs Overview + new block in the tree |
| **New subject notes** like `lab5/datatypes.md`, `labN/topic.md` | `README.md`: overview-table row (link it) + tree entry |
| **Root docs** (`README`, `LICENSE`, `CONTRIBUTING`) | Nothing else references them |
| **`setupgit.md` / `pythonsetup.md`** | Standalone personal notes — nothing depends on them |
| **`TREE.md` itself** | Nothing — but keep it the mirror of the real tree after any add/rename/delete |

**Standing rule:** every structural change (new lab, new file group, rename, delete) touches exactly three things — the file itself, the README (overview table), and this tree.
