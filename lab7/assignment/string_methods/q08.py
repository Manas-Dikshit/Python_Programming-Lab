# 8. Clean whitespace and remove a prefix/suffix
s = "  Python  "
print("strip()  :", repr(s.strip()))
print("lstrip() :", repr(s.lstrip()))
print("rstrip() :", repr(s.rstrip()))

name = "draft_report.txt"
print("removeprefix('draft_') :", name.removeprefix("draft_"))
print("removesuffix('.txt')   :", name.removesuffix(".txt"))
print("both                   :", name.removeprefix("draft_").removesuffix(".txt"))
