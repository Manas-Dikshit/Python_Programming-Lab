# Boolean datatype: True / False (subclass of int)
t = True
f = False

print("t =", t, " f =", f)
print("type(t) :", type(t))

print("t == 1  :", t == 1)   # bool is a subclass of int
print("f == 0  :", f == 0)
print("int(t)  :", int(t), " int(f) :", int(f))

# truthiness of other values
print("bool(0)     :", bool(0))
print("bool(5)     :", bool(5))
print("bool('')    :", bool(""))
print("bool('hi')  :", bool("hi"))
print("bool([])    :", bool([]))
print("bool([1])   :", bool([1]))

x, y = 10, 20
print("x < y :", x < y, " x > y :", x > y)
print("t and f:", t and f, " t or f:", t or f, " not t:", not t)
