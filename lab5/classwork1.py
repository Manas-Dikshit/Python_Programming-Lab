# String operations on "Hello Suiit"
s = "Hello Suiit"

print("s          =", s)
print("type(s)    :", type(s))
print("len(s)     :", len(s))

print("\n--- Indexing & Slicing ---")
print("s[0]      :", s[0])           # first char
print("s[-1]     :", s[-1])          # last char
print("s[0:5]    :", s[0:5])         # slice 'Hello'
print("s[6:]     :", s[6:])          # slice from 'Suiit'
print("s[::-1]   :", s[::-1])        # reverse
print("s[::2]    :", s[::2])         # every 2nd char

print("\n--- Arithmetic on strings ---")
print("'Hi ' + s :", "Hi " + s)     # concatenation
print("s[0:5] * 2:", s[0:5] * 2)    # repetition

print("\n--- Membership ---")
print("'Suiit' in s     :", "Suiit" in s)
print("'x' not in s    :", "x" not in s)
print("for loop over s :", [ch for ch in "AB"])   # iteration shown simply

print("\n--- Case methods ---")
print("s.upper()      :", s.upper())
print("s.lower()      :", s.lower())
print("s.title()      :", s.title())
print("s.capitalize() :", s.capitalize())
print("s.swapcase()   :", s.swapcase())

print("\n--- Search & count ---")
print("s.find('Suiit')   :", s.find("Suiit"))
print("s.index('l')      :", s.index("l"))
print("s.count('l')      :", s.count("l"))
print("s.startswith('He'):", s.startswith("He"))
print("s.endswith('it')  :", s.endswith("it"))

print("\n--- Modify & clean ---")
t = "  Hello Suiit  "
print("t                  :", t)
print("t.strip()          :", t.strip())
print("s.replace('l', 'L'):", s.replace("l", "L"))
print("' '.join(s)        :", " ".join(s))
print("s.split()          :", s.split())

print("\n--- Formatting ---")
print("s.center(20, '*'):", s.center(20, "*"))
print("s.ljust(15, '-') :", s.ljust(15, "-"))
print("s.rjust(15, '-') :", s.rjust(15, "-"))
print("f-string         :", f"{s} has {len(s)} characters")

print("\n--- Checking ---")
print("s.isalpha()  :", s.isalpha())      # False: space is not alpha
print("'Hello'.isalpha():", "Hello".isalpha())
print("'123'.isdigit():", "123".isdigit())
print("'Hello'.islower():", "Hello".islower(), " 'hi'.isupper():", "hi".isupper())
print("ord('A') / chr(97):", ord("A"), "/", chr(97))
