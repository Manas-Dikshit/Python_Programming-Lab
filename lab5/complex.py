# Complex datatype: real + imaginary part, written as a+bj
c1 = 3 + 4j
c2 = complex(1, 2)

print("c1 =", c1, " c2 =", c2)
print("type(c1) :", type(c1))

print("c1.real :", c1.real)
print("c1.imag :", c1.imag)
print("abs(c1) :", abs(c1))    # magnitude

print("c1 + c2 :", c1 + c2)
print("c1 * c2 :", c1 * c2)
print("c1 ** 2 :", c1 ** 2)
print("conjugate:", c1.conjugate())
