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
   git commit -m "Add lab 4 programs 1-10"
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

| Type | Example |
|------|---------|
| Add | `Add lab 4 assignment` |
| Fix | `Fix division error in program24.py` |
| Docs | `Update README structure section` |
| Refactor | `Simplify swap logic in program29.py` |

## Reporting Issues

Found a bug or an unclear explanation? Open an issue with:

- The file name and line number
- What you expected vs what happened
- The exact error message, if any

---

<div align="center">

Happy coding — made by **MRD** with **❤️**

</div>
