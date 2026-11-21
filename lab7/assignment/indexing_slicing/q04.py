# 4. Slice a list and compare a clamped slice with an invalid index
values = [10, 20, 30, 40, 50, 60]
print("values[1:5]   :", values[1:5])
print("values[-3:]   :", values[-3:])
print("values[::2]   :", values[::2])
print("values[4:1:-1]:", values[4:1:-1])
print("values[::-1]  :", values[::-1])

print("values[20:]   :", values[20:])   # slice clamps -> []
try:
    print(values[20])                   # index raises
except IndexError as e:
    print("values[20]    : IndexError:", e)
