# Ternary (conditional) operator: value_if_true if condition else value_if_false
a = 17
b = 5

print("a =", a, " b =", b)
print("larger value :", a if a > b else b)
print("smaller value:", b if b < a else a)
print("even or odd  :", "even" if a % 2 == 0 else "odd")
print("positive?    :", "positive" if a > 0 else "non-positive")
