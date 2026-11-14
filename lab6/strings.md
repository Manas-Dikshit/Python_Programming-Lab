# Python Strings — Study Notes

A `str` is an ordered sequence of characters. Strings are **immutable**: every "change" builds a new string, the original is never modified.

```python
s = "Manas Ranjan Dikshit"
s[0] = "R"        # TypeError: 'str' object does not support item assignment
s = s.replace("Manas", "R")   # new string; s now points to it
```

## Creating strings

```python
a = 'single'          # single quotes
b = "double"          # double quotes (same thing)
c = """triple
quoted"""             # spans lines, keeps \n
d = str(42)           # from another type -> "42"
```

Escapes: `\n` newline, `\t` tab, `\\` backslash, `\'` / `\"` quote.

## Indexing and slicing

```text
s = "Manas Ranjan Dikshit"
     0 1 2 3 4 5 ...        positive index from the left
    -20 ... -2 -1           negative index from the right
```

| Expression | Result | Meaning |
|---|---|---|
| `s[0]` | `M` | first character |
| `s[-1]` | `t` | last character |
| `s[0:5]` | `Manas` | start:stop — stop is **excluded** |
| `s[:5]` | `Manas` | start defaults to 0 |
| `s[6:]` | `Ranjan Dikshit` | stop defaults to end |
| `s[::-1]` | `tihskiD najnaR sanaM` | step -1 reverses |
| `s[::2]` | `MnsRna isi` | every second character |

The index can be **any expression** — Python evaluates it first:

```python
s[1 + 5]        # same as s[6]   -> 'R'
s[2 * 3]        # same as s[6]   -> 'R'
s[len(s) - 1]   # last char      -> 't'
s[1 + 2:4 * 2]  # slice is s[3:8] -> 'as Ra'
```

Out-of-range single index raises `IndexError`; a slice never does — it just clamps (`s[0:100]` returns the whole string).

## Common methods

All methods return a **new** string; `s` is unchanged.

| Method | Example | Result |
|---|---|---|
| `upper()` / `lower()` | `s.upper()` | `MANAS RANJAN DIKSHIT` |
| `title()` | `s.title()` | `Manas Ranjan Dikshit` |
| `swapcase()` | `s.swapcase()` | `mANAS rANJAN dIKSHIT` |
| `strip()` / `lstrip()` / `rstrip()` | `"  hi  ".strip()` | `hi` |
| `replace(old, new)` | `s.replace("Ranjan", "R")` | `Manas R Dikshit` |
| `find(sub)` / `rfind(sub)` | `s.find("a")` | `1` / `10`, `-1` if absent |
| `count(sub)` | `s.count("a")` | `4` |
| `split()` / `split(",")` | `s.split()` | `['Manas', 'Ranjan', 'Dikshit']` |
| `join(iterable)` | `"-".join(["a", "b"])` | `a-b` |
| `startswith()` / `endswith()` | `s.startswith("Manas")` | `True` |
| `partition(sep)` | `s.partition(" ")` | `('Manas', ' ', 'Ranjan Dikshit')` |
| `isdigit()` / `isalpha()` / `isspace()` | `"42".isdigit()` | `True` |
| `zfill(width)` | `"7".zfill(3)` | `007` |

`find()` returns `-1` when the substring is missing; `index()` raises `ValueError` instead. Prefer `in` for a plain yes/no test:

```python
"Ranjan" in s        # True
```

## Joining and splitting

`split()` breaks a string into a list; `join()` is its inverse. `join()` is called on the **separator**, not on the list:

```python
words = s.split()                 # ['Manas', 'Ranjan', 'Dikshit']
"-".join(words)                   # 'Manas-Ranjan-Dikshit'
", ".join(["a", "b", "c"])        # 'a, b, c'
```

Repeated `+` in a loop is slow (each `+` copies the whole string) — collect pieces in a list and `join()` once.

## Concatenation, repetition, formatting

```python
"ab" + "cd"        # 'abcd'
"py" * 3           # 'pypypy'
f"{s} has {len(s)} characters"    # f-string, Python 3.6+
"{} scored {}".format("Ravi", 91) # older .format() style
```

Use f-strings by default; they are the shortest and fastest.

## Operators (vs methods)

Strings have operators too; unlike methods they need no parentheses. `[i]`, `[a:b]` are slicing, not operators.

| Operator | Example | Result |
|---|---|---|
| `+` | `"ab" + "cd"` | `abcd` — concatenate |
| `*` | `"py" * 3` | `pypypy` — repeat |
| `in` / `not in` | `"ell" in "Hello"` | `True` — substring test |
| `%` | `"%s scored %d" % ("Manas", 91)` | `Manas scored 91` — old-style formatting |
| `==` / `!=` | `"a" == "A"` | `False` — content comparison |
| `<` `>` `<=` `>=` | `"Z" < "a"` | `True` — lexicographic (code point) |
| `is` / `is not` | `x is z` | object identity, **not** content — use `==` for text |
| `and` / `or` / `not` | `"" or "default"` | returns an operand; `""` is falsy → `default` |
| `+=` / `*=` | `d += "ha"` | rebuilds a new string (same as `d = d + "ha"`) |

`%s` takes a string, `%d` an integer, `%f` a float; widths and alignment: `"|%10s|"` right, `"|%-10s|"` left. Prefer f-strings for new code.

## Comparing strings

`==` compares content, `is` compares identity (rarely what you want). Ordering is by Unicode code point, so `"Z" < "a"` is `True` and uppercase sorts before lowercase. Compare case-insensitively with `.lower()` on both sides.

## Immutability — the key exam idea

```python
a = "hi";  b = a;  a = a + "!"   # b is still "hi" — a now points to a new object
```

Since strings cannot change, they are hashable: usable as `dict` keys and `set` members. Building a big string with `+=` is fine for a few joins; for thousands, use a list and `join()`.

## Quick reference

| Need | Use |
|---|---|
| length | `len(s)` |
| character at position | `s[i]`, `s[-1]` for last |
| part of a string | `s[start:stop:step]` |
| yes/no substring test | `sub in s` |
| position of substring | `s.find(sub)` |
| clean user input | `s.strip().lower()` |
| text ↔ list | `s.split()`, `sep.join(list)` |
| build output | f-strings `f"{x}"` |
