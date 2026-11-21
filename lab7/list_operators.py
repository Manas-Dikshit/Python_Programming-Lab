# List operators: + * in / not in [] comparison is logical and unpacking
a = [1, 2, 3]
b = [4, 5]

# + concatenation, * repetition (lists are mutable, unlike strings)
print("a + b        :", a + b)
print("a * 3        :", a * 3)
print("[0] * 4      :", [0] * 4)
print("a is a+b     :", a is a + b)   # + always builds a new list

# += and *= modify the list in place
c = [1, 2]
c += [3]
c *= 2
print("c += then *= :", c)
print("a unchanged  :", a)

# membership: in / not in
print("2 in a       :", 2 in a)
print("9 not in a   :", 9 not in a)

# [] indexing, negative indexing, slicing, step
print("a[0]         :", a[0])
print("a[-1]        :", a[-1])
print("a[1:3]       :", a[1:3])
print("a[::-1]      :", a[::-1])

# item and slice assignment (lists are mutable)
d = a[:]
d[0] = 99
d[1:3] = [7, 8, 9]
print("d after set  :", d)

# comparison: lexicographic, element by element
print("[1,2] == [1,2] :", [1, 2] == [1, 2])
print("[1,2] < [1,3]  :", [1, 2] < [1, 3])
print("[1,2] != [2,1] :", [1, 2] != [2, 1])

# identity vs content
e = a
print("a == e       :", a == e)
print("a is e       :", a is e)      # same object
print("a is a[:]    :", a is a[:])   # slice makes a copy

# logical: empty list is falsy; and/or return an operand
empty = []
print("not empty    :", not empty)
print("empty or a   :", empty or a)

# unpacking with * (Python 3.5+)
print("[*a, *b]     :", [*a, *b])
first, *rest = a
print("first, rest  :", first, rest)
