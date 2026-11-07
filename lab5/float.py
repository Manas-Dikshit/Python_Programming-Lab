# Float datatype: real numbers with a decimal point
x = 10.5
y = -3.2
z = 2.5e3   # scientific notation -> 2500.0

print("x =", x, " y =", y, " z =", z)
print("type(x) :", type(x))

print("x + y :", x + y)
print("x / 2 :", x / 2)
print("round(x, 1) :", round(x, 1))

pi = 3.14159
print("pi =", pi, " approx =", round(pi, 2))

print("float('7')   :", float("7"))
print("float(1)     :", float(1))
print("int(10.9)    :", int(10.9))   # truncates, does not round
print("abs(y)       :", abs(y))
