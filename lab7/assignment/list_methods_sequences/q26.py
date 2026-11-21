# 26. Iterate and test sequences with zip/enumerate/any/all
names = ["Riya", "Aman"]
marks = [72, 38]
pass_mark = 40

for i, (name, mark) in enumerate(zip(names, marks), 1):
    print(i, name, mark)

print("any failed:", any(mark < pass_mark for mark in marks))
print("all passed:", all(mark >= pass_mark for mark in marks))
