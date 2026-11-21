# 9. Search and count "ana" in "banana"
s = "banana"
print("find('ana')   :", s.find("ana"))
print("rfind('ana')  :", s.rfind("ana"))
print("index('ana')  :", s.index("ana"))
print("rindex('ana') :", s.rindex("ana"))
print("count('ana')  :", s.count("ana"))

# Missing substring: find() returns -1, index() raises ValueError
print("find('xyz')   :", s.find("xyz"))
try:
    print(s.index("xyz"))
except ValueError as e:
    print("index('xyz')  : ValueError:", e)
