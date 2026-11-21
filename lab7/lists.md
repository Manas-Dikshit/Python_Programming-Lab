# Python Lists — Study Notes

A `list` is an **ordered, mutable** sequence that allows duplicates and mixed types. It is written with square brackets.

```python
nums = [10, 20, 30]
mixed = [1, "two", 3.0, True]
empty = []
from_range = list(range(5))   # [0, 1, 2, 3, 4]
```

## Indexing and slicing

```text
nums = [10, 20, 30, 40]
         0   1   2   3      positive index from the left
        -4  -3  -2  -1      negative index from the right
```

| Expression | Result | Meaning |
|---|---|---|
| `nums[0]` | `10` | first item |
| `nums[-1]` | `40` | last item |
| `nums[1:3]` | `[20, 30]` | start:stop — stop is **excluded** |
| `nums[:2]` | `[10, 20]` | start defaults to 0 |
| `nums[2:]` | `[30, 40]` | stop defaults to end |
| `nums[::-1]` | `[40, 30, 20, 10]` | step -1 reverses |
| `nums[::2]` | `[10, 30]` | every second item |

An index out of range raises `IndexError`; a slice never does — it clamps (`nums[0:100]` returns all items).

## Mutability

Lists can be changed **in place** — the object keeps the same `id()`:

```python
nums = [10, 20, 30]
nums[1] = 99          # change one item
nums[0], nums[2] = 7, 8   # change two positions at once
nums[1:3] = [5, 6, 7]     # slice assignment can change the length
print(id(nums))       # same id before and after
```

Strings are immutable by contrast: `s.upper()` returns a new string; `s[0] = "x"` raises `TypeError`.

## Operators

| Operator | Example | Result |
|---|---|---|
| `+` | `[1] + [2]` | `[1, 2]` — new list |
| `*` | `[0] * 3` | `[0, 0, 0]` |
| `+=` / `*=` | `a += [3]` | modifies `a` in place (unlike `a = a + [3]`) |
| `in` / `not in` | `2 in [1, 2]` | `True` — membership test |
| `==` / `!=` | `[1, 2] == [1, 2]` | content comparison |
| `<` `>` `<=` `>=` | `[1, 2] < [1, 3]` | lexicographic, element by element |
| `is` / `is not` | `a is a[:]` | `False` — identity, not content |

`[*a, *b]` unpacks lists into a new one; `first, *rest = nums` takes the first item and the remainder.

## Built-in functions

| Function | Example | Result |
|---|---|---|
| `len(lst)` | `len([1, 2])` | `2` |
| `min(lst)` / `max(lst)` | `max([3, 1])` | `3` |
| `sum(lst)` | `sum([1, 2, 3])` | `6` — numbers only |
| `sorted(lst)` | `sorted([3, 1])` | `[1, 3]` — new list; `reverse=True` for descending |
| `list(x)` | `list("ab")` | `['a', 'b']` — from any iterable |
| `enumerate(lst, 1)` | `list(enumerate(["a"], 1))` | `[(1, 'a')]` — index + value |
| `zip(a, b)` | `list(zip([1], ["a"]))` | `[(1, 'a')]` — pair up; `zip(*rows)` transposes |
| `any(lst)` / `all(lst)` | `all([1, 2])` | `True` — truthiness test |
| `reversed(lst)` | `list(reversed([1, 2]))` | `[2, 1]` — iterator, not a list |

`min`/`max`/`sum` on an empty list raise `ValueError` (except `sum([])`, which is `0`).

## List methods

All 11 methods of `list`:

| Method | What it does | In place? |
|---|---|:---:|
| `append(x)` | add `x` at the end | ✓ |
| `insert(i, x)` | add `x` before index `i` | ✓ |
| `extend(iterable)` | add all items from another iterable | ✓ |
| `remove(x)` | delete first item equal to `x` | ✓ |
| `pop(i)` | remove and return item at `i` (default last) | ✓ |
| `clear()` | remove all items | ✓ |
| `sort()` | sort in place; `key=`, `reverse=True` supported | ✓ |
| `reverse()` | reverse in place | ✓ |
| `count(x)` | how many items equal `x` | ✗ |
| `index(x)` | first position of `x` | ✗ |
| `copy()` | shallow copy | ✗ |

`remove(x)` raises `ValueError` and `index(x)` raises `ValueError` if the item is missing. `sort()` changes the list and returns `None`; `sorted()` returns a new list — assigning `lst = lst.sort()` makes `lst` become `None`.

## Iteration

```python
for item in nums: ...                  # values
for i in range(len(nums)): ...         # indexes
for i, item in enumerate(nums, 1): ... # both, starting at 1
for a, b in zip(list_a, list_b): ...   # pairs

i = 0                                  # while loop with an index
while i < len(nums):
    print(nums[i])
    i += 1
```

Do not remove items while iterating the same list — items get skipped. Iterate over a copy instead:

```python
for n in nums[:]:
    if n % 2 == 0:
        nums.remove(n)
```

## Comprehensions and advanced patterns

```python
squares = [x * x for x in range(6)]            # transform
evens = [x for x in range(10) if x % 2 == 0]  # filter
flat = [x for row in grid for x in row]        # flatten nested lists
```

| Tool | Use |
|---|---|
| `map(fn, lst)` | apply `fn` to each item — often a comprehension is clearer |
| `filter(fn, lst)` | keep items where `fn(item)` is truthy |
| `reduce(fn, lst)` | combine items into one value (`from functools import reduce`) |
| `sorted(lst, key=len)` | custom order using a function |
| `any(...)` / `all(...)` | check truthiness across items |

## Copying: shallow vs deep

```python
grid = [[1, 2], [3, 4]]
shallow = grid.copy()      # outer list copied, inner lists shared
deep = deepcopy(grid)      # from copy import deepcopy — fully independent
grid[0][0] = 99
# shallow -> [[99, 2], [3, 4]]   deep -> [[1, 2], [3, 4]]
```

`list()`/`copy()`/`[:]` are all shallow. Use `deepcopy()` for nested structures.

## Common mistakes

| Mistake | Fix |
|---|---|
| `lst[3]` on a 3-item list | use index `2`; first index is 0 |
| expecting `lst[1:3]` to include index 3 | stop index is excluded |
| `lst = lst.sort()` | use `lst.sort()` or `lst = sorted(lst)` |
| `nums * 0` reuse pitfalls with nested lists (`[[0]] * 3` shares rows) | use `[[0] for _ in range(3)]` |
| removing while iterating | loop over `lst[:]` |
| expecting `remove(99)` to be silent | it raises `ValueError` for a missing value |

## Quick reference

| Need | Use |
|---|---|
| length | `len(lst)` |
| item at position | `lst[i]`, `lst[-1]` for last |
| part of the list | `lst[start:stop:step]` |
| add one item | `append(x)` / `insert(i, x)` |
| add many items | `extend(iterable)` / `+` |
| delete | `del lst[i]`, `remove(x)`, `pop(i)`, `clear()` |
| find position | `index(x)` / `x in lst` |
| sort | `sort()` in place / `sorted()` new list |
| build from a loop | list comprehension |
| independent copy of nested list | `deepcopy(lst)` |
