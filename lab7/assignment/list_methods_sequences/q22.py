# 22. Locate and count elements safely
letters = ["A", "B", "A", "C"]
print("index('A'):", letters.index("A"))
print("count('A'):", letters.count("A"))

if "D" in letters:              # membership test before index()
    print("index('D'):", letters.index("D"))
else:
    print("Not found")
