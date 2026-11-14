# Contributing to Python Programming Lab

Thanks for your interest in improving **PP_Lab**. Follow these simple guidelines to keep the repository clean and consistent.

## How to Contribute

1. **Fork** the repository.
2. **Clone** your fork:

   ```sh
   git clone https://github.com/<your-username>/Python_Programming-Lab.git
   cd Python_Programming-Lab
   ```

3. **Create a new branch**:

   ```sh
   git checkout -b feature/lab4-programs
   ```

4. **Make your changes** (see conventions below).
5. **Commit** with a clear message:

   ```sh
   git commit -m "feat: add lab 4 programs 1-10"
   ```

6. **Push** and open a **Pull Request**:

   ```sh
   git push origin feature/lab4-programs
   ```

## Coding Conventions

- One program per file. Lab programs go in `lab<N>/` as `programNN.py` or a descriptive name (`labactivityN.py`).
- Start every file with a one-line comment describing what the program does.
- Keep it simple: plain scripts with `input()` / `print()`, no external libraries unless required.
- Use meaningful variable names (`total_marks` over `tm`).
- Verify your code runs before submitting:

  ```sh
  python lab3\program01.py
  ```

## Commit Message Style

Use `type: subject` — lowercase type, then a short imperative subject (no trailing period, ~50 chars):

```text
feat: add lab 6 string operations program
fix: handle divide-by-zero in program24.py
docs: update README lab overview table
refactor: simplify swap logic in program29.py
chore: ignore __pycache__ and editor files
```

| Type | Use for | Example |
|------|---------|---------|
| `feat` | New program, lab, or file | `feat: add lab 6 strings notes` |
| `fix` | Correcting broken code | `fix: correct temperature conversion formula` |
| `docs` | README, notes, `TREE.md`, comments | `docs: add lab6 to project tree` |
| `refactor` | Same behavior, cleaner code | `refactor: extract area calculation` |
| `chore` | Tooling, `.gitignore`, housekeeping | `chore: add Python .gitignore` |

## Reporting Issues

Found a bug or an unclear explanation? Open an issue with:

- The file name and line number
- What you expected vs what happened
- The exact error message, if any

---

<div align="center">

Happy coding — made by **MRD** with **❤️**

</div>
