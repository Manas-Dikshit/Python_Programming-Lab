# Calculate area and circumference of a circle.
import math

radius = float(input("Enter radius: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("Area          =", area)
print("Circumference =", circumference)
