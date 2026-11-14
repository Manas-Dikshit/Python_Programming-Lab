# String operators: + * in / not in % == != < > is and or not (not methods)
a = "Hello"
b = "Suiit"

# + concatenation and * repetition
print("a + ' ' + b :", a + " " + b)
print("a * 3        :", a * 3)
print("a * 0        :", repr(a * 0))          # repetition by 0 gives ''
print("'=' * 20     :", "=" * 20)

# membership: in / not in
print("'ell' in a        :", "ell" in a)
print("'xyz' not in a    :", "xyz" not in a)

# % old-style formatting
name, marks = "Manas", 91
print("'%s scored %d'   :", "%s scored %d" % (name, marks))
print("'%10s|'          :", "|%10s|" % name)   # right aligned, width 10
print("'%-10s|'         :", "|%-10s|" % name)  # left aligned, width 10

# comparison: lexicographic by Unicode code point
print("a == b       :", a == b)
print("a != b       :", a != b)
print("a < b        :", a < b)
print("'Z' < 'a'    :", "Z" < "a")          # uppercase sorts first
print("'abc' < 'abd' :", "abc" < "abd")
print("'abc' <= 'abc':", "abc" <= "abc")
print("'abd' >= 'abc':", "abd" >= "abc")

# identity: is / is not compare objects, == compares content
x = "hi"
y = "hi"
z = "".join(["h", "i"])       # built at runtime, equal but a different object
print("x == y       :", x == y)
print("x is y       :", x is y)   # same interned literal
print("x == z       :", x == z)
print("x is z       :", x is z)   # False — equal content, different object
print("x is not z   :", x is not z)

# logical: and / or return an operand, not True/False; '' is falsy
empty = ""
print("not empty    :", not empty)
print("empty or 'default' :", empty or "default")   # first truthy operand
print("a and 'ok'   :", a and "ok")                 # last operand if all truthy

# immutable but "editable": rebuild with operators
c = a
c += "!"
print("c            :", c, "| a still:", a)

d = "ha"
d += "ha"
d *= 2
print("d += then *= :", d)
