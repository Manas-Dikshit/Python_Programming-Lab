# Advanced list techniques: map/filter/reduce, key=, unpacking, deepcopy
from functools import reduce
from copy import deepcopy

nums = [1, 2, 3, 4, 5, 6]

# map() transforms every item; a comprehension does the same more simply
print("map doubled :", list(map(lambda x: x * 2, nums)))
print("comprehension:", [x * 2 for x in nums])

# filter() keeps only items that pass the test
print("filter evens:", list(filter(lambda x: x % 2 == 0, nums)))

# reduce() combines all items into one value
print("reduce sum  :", reduce(lambda a, b: a + b, nums))

# key= customises sorted(), min() and max()
words = ["apple", "kiwi", "banana"]
print("by length   :", sorted(words, key=len))
print("max by len  :", max(words, key=len))
people = [("Manas", 91), ("deba", 88), ("Asha", 95)]
print("by marks    :", sorted(people, key=lambda p: p[1]))

# any() / all() with generator expressions
print("any even    :", any(n % 2 == 0 for n in nums))
print("all positive:", all(n > 0 for n in nums))

# enumerate(start), zip() and zip(*rows) to transpose
print("enum from 1 :", list(enumerate(words, 1)))
names, marks = zip(*people)
print("transposed  :", names, marks)
print("paired back :", list(zip(names, marks)))

# nested comprehension flattens a list of lists
grid = [[1, 2], [3, 4]]
print("flatten     :", [x for row in grid for x in row])

# extended unpacking with *
first, *middle, last = nums
print("unpack      :", first, middle, last)

# shallow copy vs deep copy of nested lists
shallow = grid.copy()
deep = deepcopy(grid)
grid[0][0] = 99
print("shallow     :", shallow)   # inner list is shared, so it changed
print("deep        :", deep)      # fully independent copy
