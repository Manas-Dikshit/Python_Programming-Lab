# upper(), find(), count() on two strings
s1 = "hello suiit"
s2 = "happy childrens day"

print("s1             :", s1)
print("s2             :", s2)

# upper() -> new uppercase string, original unchanged
print("s1.upper()     :", s1.upper())
print("s2.upper()     :", s2.upper())

# find() -> position of substring, -1 when absent
print("s1.find('suiit')      :", s1.find("suiit"))
print("s2.find('childrens')  :", s2.find("childrens"))
print("s2.find('day')        :", s2.find("day"))
print("s1.find('z')          :", s1.find("z"))

# count() -> how many times substring occurs
print("s1.count('i')         :", s1.count("i"))
print("s2.count('p')         :", s2.count("p"))
print("s2.count(' ')         :", s2.count(" "))
print("s2.count('day')       :", s2.count("day"))

# count() is case-sensitive, so upper() first when needed
print("s2.upper().count('P') :", s2.upper().count("P"))
