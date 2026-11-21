# 7. Apply all case-conversion methods to the same string
s = "pYtHon Straße"
print("original    :", s)
print("lower()     :", s.lower())
print("upper()     :", s.upper())
print("capitalize():", s.capitalize())
print("title()     :", s.title())
print("swapcase()  :", s.swapcase())
print("casefold()  :", s.casefold())
# lower() keeps ß; casefold() converts it to "ss"
