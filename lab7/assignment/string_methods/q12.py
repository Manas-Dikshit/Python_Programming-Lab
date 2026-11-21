# 12. Split once from each side, splitlines and join
s = "red,green,blue"
print("split(',', 1)  :", s.split(",", 1))
print("rsplit(',', 1) :", s.rsplit(",", 1))

lines = "red\ngreen\nblue".splitlines()
print("splitlines()   :", lines)
print("join(' | ')    :", " | ".join(lines))
