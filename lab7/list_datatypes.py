# Different data types of lists and operations on each
ints = [5, 2, 9, 2]
floats = [3.5, 1.2, 4.8]
words = ["banana", "apple", "cherry"]
flags = [True, False, True]
mixed = [10, "hi", 3.5, True, None]
nested = [[1, 2], [3, 4]]
pairs = [("Manas", 91), ("Ravi", 88)]
students = [{"name": "Manas", "marks": 91}, {"name": "Ravi", "marks": 88}]

# list of int: sum, min, max, sorted, comprehension
print("ints       :", ints)
print("sum/min/max:", sum(ints), min(ints), max(ints))
print("sorted     :", sorted(ints))
print("squares    :", [x * x for x in ints if x % 2 != 0])

# list of float: average and rounding
avg = sum(floats) / len(floats)
print("floats     :", floats)
print("average    :", round(avg, 2), "| rounded:", [round(x) for x in floats])

# list of str: join, sort, upper, length of each
print("words      :", words)
print("joined     :", ", ".join(words))
print("sorted     :", sorted(words))
print("upper      :", [w.upper() for w in words], "| lengths:", [len(w) for w in words])

# list of bool: count and all/any
print("flags      :", flags)
print("count T/F  :", flags.count(True), flags.count(False))
print("all()/any():", all(flags), any(flags))

# mixed list: inspect what each element actually is
print("mixed      :", mixed)
print("types      :", [type(x).__name__ for x in mixed])
print("only str   :", [x for x in mixed if isinstance(x, str)])

# list of lists: flatten and index into it
print("nested     :", nested, "| nested[1][0]:", nested[1][0])
print("flattened  :", [x for row in nested for x in row])

# list of tuples: sort by the second item, unpack in a loop
print("pairs      :", sorted(pairs, key=lambda p: p[1]))
print("names      :", [name for name, marks in pairs])

# list of dicts: filter and sort by a key
print("students   :", students)
print("toppers    :", [s["name"] for s in students if s["marks"] >= 90])
print("by marks   :", sorted(students, key=lambda s: s["marks"], reverse=True))

# empty list and conversion from other sequences
print("empty      :", [], "| bool:", bool([]))
print("from str   :", list("abc"), "| from range:", list(range(3)))
