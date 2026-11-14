# String operations: create, index, slice, search, transform, split/join
s = "Manas Ranjan Dikshit"

print("s            =", s)
print("type(s)      :", type(s))
print("len(s)       :", len(s))

# Indexing and slicing
print("s[0]         :", s[0])          # first character
print("s[-1]        :", s[-1])         # last character
print("s[0:5]       :", s[0:5])        # slicing
print("s[::-1]      :", s[::-1])        # reverse
print("s[::2]       :", s[::2])        # every second character

# Case conversion
print("s.upper()    :", s.upper())
print("s.lower()    :", s.lower())
print("s.title()    :", s.title())
print("s.swapcase() :", s.swapcase())

# Searching and counting
print("s.find('a')  :", s.find("a"))
print("s.rfind('a') :", s.rfind("a"))
print("s.count('a') :", s.count("a"))
print("'Ranjan' in s:", "Ranjan" in s)
print("s.startswith('Manas') :", s.startswith("Manas"))
print("s.endswith('Dikshit')  :", s.endswith("Dikshit"))

# Replace, strip, split and join
print("s.replace('Ranjan', 'R') :", s.replace("Ranjan", "R"))
t = "  padded  "
print("t.strip()    :", repr(t.strip()))
print("t.lstrip()   :", repr(t.lstrip()))
print("t.rstrip()   :", repr(t.rstrip()))
words = s.split()
print("s.split()    :", words)
print("'-'.join(words) :", "-".join(words))
print("s.partition(' ') :", s.partition(" "))

# Concatenation, repetition and formatting
print("'ab' + 'cd'  :", "ab" + "cd")
print("'py' * 3     :", "py" * 3)
print(f"{s} has {len(s)} characters")

# Immutability: strings cannot be changed in place
try:
    s[0] = "R"
except TypeError as e:
    print("s[0] = 'R'   : TypeError:", e)
