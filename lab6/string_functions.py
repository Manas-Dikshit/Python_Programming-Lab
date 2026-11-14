# String functions and methods: built-ins that take a string + str methods
s = "  Manas  "
name = "manas ranjan dikshit"

# Built-in functions that work on strings
print("len(s)        :", len(s))
print("str(42)       :", str(42), type(str(42)))
print("ord('A')      :", ord("A"))          # character -> code point
print("chr(97)       :", chr(97))            # code point -> character
print("min('bca')    :", min("bca"))
print("max('bca')    :", max("bca"))
print("sorted('bca') :", sorted("bca"))
print("list('abc')   :", list("abc"))
print("repr(s)       :", repr(s))            # quotes + escapes shown
print("ascii('café') :", ascii("café"))      # non-ASCII escaped

# Case and padding
print("capitalize()       :", name.capitalize())
print("casefold()         :", name.casefold())
print("center(26, '*')    :", name.center(26, "*"))
print("ljust(26, '.')     :", name.ljust(26, "."))
print("rjust(26, '.')     :", name.rjust(26, "."))
print("'7'.zfill(3)       :", "7".zfill(3))

# Search — find() returns -1, index() raises ValueError when missing
print("find('ranjan')     :", name.find("ranjan"))
print("rfind('a')         :", name.rfind("a"))
print("index('ranjan')    :", name.index("ranjan"))
try:
    name.index("xyz")
except ValueError as e:
    print("index('xyz')       : ValueError:", e)

# Character tests
print("'42'.isdigit()     :", "42".isdigit())
print("'abc'.isalpha()    :", "abc".isalpha())
print("'abc1'.isalnum()   :", "abc1".isalnum())
print("'   '.isspace()    :", "   ".isspace())
print("'abc'.islower()    :", "abc".islower())
print("'ABC'.isupper()    :", "ABC".isupper())
print("'Hello World'.istitle() :", "Hello World".istitle())

# Translate — map characters through a table
table = str.maketrans("aeiou", "AEIOU")
print("translate(table)   :", name.translate(table))

# Other formatting styles
print("format()           :", "{} is {}".format("Python", "fun"))
print("% formatting       :", "%s has %d labs" % ("PP_Lab", 6))
