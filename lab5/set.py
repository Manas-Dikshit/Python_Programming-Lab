# Set datatype: unordered, mutable, NO duplicates
a = {1, 2, 3, 3, 2}
b = {3, 4, 5}

print("a (duplicates removed) =", a)
print("b =", b)
print("type(a) :", type(a))

empty = set()               # not {} (that makes a dict)
empty.add(1)
empty.add(1)
print("empty after adding 1 twice:", empty)

a.add(6)
a.discard(1)
print("a after add(6)/discard(1) :", a)

print("a | b (union)       :", a | b)
print("a & b (intersection):", a & b)
print("a - b (difference)  :", a - b)
print("a ^ b (symmetric diff):", a ^ b)
print("len(a) :", len(a))
