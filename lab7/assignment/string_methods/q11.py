# 11. Replace hyphens, then translate hyphens to underscores and drop digits
s = "Room-101-A"
print("replace('-', ' ') :", s.replace("-", " "))

table = str.maketrans("-", "_", "0123456789")
print("translate(table)  :", s.translate(table))
