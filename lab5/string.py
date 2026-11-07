# String datatype: sequence of characters, immutable
s = "Manas Ranjan Dikshit"
print("s        =", s)
print("type(s)  :", type(s))

print("s[0]     :", s[0])        # indexing
print("s[0:6]   :", s[0:6])      # slicing
print("len(s)   :", len(s))

print("s.upper()      :", s.upper())
print("s.lower()      :", s.lower())
print("s.replace('P', 'J') :", s.replace("P", "J"))
print("s.count('m')   :", s.count("m"))
print("s.split()      :", s.split())
print("'code' in s    :", "code" in s)

t = " hello "
print("t.strip():", t.strip(), "| concat:", "ab" + "cd", "| repeat:", "py" * 3)
print("f-string :", f"{s} has {len(s)} chars")
