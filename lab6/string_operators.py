# String operators: + * in / not in % == != < > (not methods)
a = "Hello"
b = "Suiit"

# + concatenation and * repetition
print("a + ' ' + b :", a + " " + b)
print("a * 3        :", a * 3)
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

# immutable but "editable": rebuild with operators
c = a
c += "!"
print("c            :", c, "| a still:", a)
