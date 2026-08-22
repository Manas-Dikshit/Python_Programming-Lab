# Exchange values of three variables in a circular manner (A -> B, B -> C, C -> A).
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
c = int(input("Enter value of C: "))

print("Before exchange: A =", a, ", B =", b, ", C =", c)

temp = a
a = c
c = b
b = temp

print("After exchange : A =", a, ", B =", b, ", C =", c)
