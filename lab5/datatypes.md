# Python Data Types — Study Notes

Data types define what kind of value a variable holds and what operations are valid on it. Python variables are just *names bound to objects* — the value carries its type, not the variable (dynamic typing).

```python
x = 42          # int
x = "forty-two" # now a str — same variable, different type
type(x)         # <class 'str'>
```

## Classification

```text
Standard data types
├── Numeric        int, float, complex
├── Boolean        bool (True / False)
├── Sequence type  str, list, tuple   (ordered, indexable)
├── Set type       set, frozenset     (unordered, no duplicates)
```

## Numeric types

| Type | Example | Notes |
|------|---------|-------|
| `int` | `42`, `-7` | Whole numbers, unlimited size. Also written in binary `0b101`, octal `0o17`, hex `0x2A` |
| `float` | `10.5`, `2.5e3` | Real numbers with a decimal point; limited precision (~15–17 digits). `2.5e3` = 2500.0 |
| `complex` | `3 + 4j` | Real + imaginary part; read as `.real` / `.imag`; `abs(c)` gives the magnitude |

Integer division stays an int: `7 // 2 == 3` and the remainder `7 % 2 == 1`. Power is `**`, so `2 ** 10 == 1024`.

## Boolean (`bool`)

- Only two values: `True` and `False` (capitalized). `bool` is a subclass of `int`, so `True == 1` and `False == 0`.
- Truthiness rules — these values are "falsy", everything else is "truthy":

| Falsy | | |
|---|---|---|
| `0`, `0.0`, `0j` | `""` (empty string) | `[]`, `()`, `{}`, `set()` |

- `0` is falsy nowhere else — `bool(-1)` is `True`.

## Sequence types

All support: indexing `s[0]`, negative indexing `s[-1]`, slicing `s[1:4]`, `len()`, `in`, `min()`, `max()`.

### `str` — text, IMMUTABLE

- Defined with single, double, or triple quotes; escape with `\n`, `\t`, `\\`.
- Methods return *new* strings (the original never changes): `upper()`, `lower()`, `strip()`, `replace()`, `split()`, `count()`, `find()`.
- Concatenate with `+`, repeat with `*`, format with f-strings: `f"{name} scored {marks}"`.

### `list` — ordered, MUTABLE

```python
nums = [10, 20, 30]
nums.append(40)      # add at end
nums.insert(0, 5)    # add at position
nums.remove(20)      # remove first occurrence by value
last = nums.pop()    # remove & return last item
nums.reverse(); nums.sort()
sorted(nums)         # returns a new sorted list, original untouched
```

- Allows duplicates and mixed types: `[1, "two", 3.0, True]`.
- Common bug: `list[-1]` is the last element, `list[1:3]` excludes index 3.

### `tuple` — ordered, IMMUTABLE

```python
point = (10, 20, 30)
single = (5,)        # single element needs the comma
x, y, z = point      # tuple unpacking
```

- Once created, items cannot be added, removed, or reassigned.
- Lighter and faster than lists; use for data that should not change (coordinates, constants).
- Methods are read-only: `count()`, `index()`.

## Set types

### `set` — unordered, MUTABLE, unique elements

```python
a = {1, 2, 3, 3}     # -> {1, 2, 3}
empty = set()        # {} is a dict, not a set!
a.add(6); a.discard(1)
a | b   # union        a & b   # intersection
a - b   # difference    a ^ b   # symmetric difference
```

- No indexing or slicing — elements are unordered.
- Removes duplicates automatically; ideal for membership tests (`x in s` is O(1)).

### `frozenset` — IMMUTABLE set

Same set operations, but no `add`/`discard`/`remove`. Because it cannot change, it can be used as a dictionary key or nested inside another set.

## Mapping type — `dict`

Key → value pairs; keys are unique and must be immutable (str, number, tuple). Values can be anything.

```python
student = {"name": "Manas", "age": 19}
student["branch"] = "CSE"     # add
student["age"] = 20           # update
del student["cgpa"]           # delete
student.get("branch", "n/a")  # safe access — no KeyError
student.items()               # keys() / values() / items()
for key, value in student.items(): ...
```

`d[key]` raises `KeyError` for a missing key; `d.get(key)` returns `None` (or a default) instead.

## Mutability — the key exam idea

| Mutable (can change in place) | Immutable (cannot change) |
|---|---|
| list, dict, set | int, float, complex, str, tuple, bool, frozenset |

Immutable values are replaced, not modified — a "changed" string is actually a new object. This is why a mutable object (`list`, `dict`, `set`) can be edited but not used as a dict key, while immutable ones can.

```python
a = "hi";  b = a;  a = a + "!"   # b is still "hi"  (str: new object)
x = [1];    y = x;  x.append(2)   # y is [1, 2] too  (list: same object)
```

## Type checking & conversion

```python
type(x)              # exact class
isinstance(x, int)   # True also for bool (bool is a subclass of int)
int("42")            # str -> int
float("3.5")         # str -> float
str(10.9)            # -> "10.9"
list("abc")          # -> ['a', 'b', 'c']
set([1, 1, 2])       # -> {1, 2}   common de-duplication trick
tuple([1, 2])        # -> (1, 2)
```

`int(10.9)` truncates toward zero (`10`), it does not round — use `round(10.9)` for rounding.

## One-line summary per type

| Type | Ordered? | Mutable? | Duplicates? | Typical use |
|------|:---:|:---:|:---:|-------------|
| int / float / complex | – | ✗ | – | numbers |
| bool | – | ✗ | – | True/False logic |
| str | ✓ | ✗ | ✓ | text |
| list | ✓ | ✓ | ✓ | collecting items |
| tuple | ✓ | ✗ | ✓ | fixed records |
| set | ✗ | ✓ | no | membership, de-dup |
| frozenset | ✗ | ✗ | no | permanent membership |
| dict | ✓ (insertion order) | ✓ | keys unique | lookups |
