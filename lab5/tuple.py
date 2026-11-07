# Tuple datatype: ordered but IMMUTABLE, allows duplicates
point = (10, 20, 30)
single = (5,)          # single-element tuple needs the comma
colors = ("red", "green", "blue", "red")

print("point  =", point)
print("single =", single)
print("colors =", colors)
print("type(point) :", type(point))

print("point[0]  :", point[0])
print("point[-1] :", point[-1])
print("point[0:2]:", point[0:2])

print("colors.count('red') :", colors.count("red"))
print("colors.index('green') :", colors.index("green"))
print("len(colors) :", len(colors))

a, b, c = point          # unpacking
print("unpacked:", a, b, c)
print("max(point) :", max(point), " min(point) :", min(point))
