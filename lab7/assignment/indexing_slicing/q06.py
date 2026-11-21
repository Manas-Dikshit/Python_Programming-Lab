# 6. Compare strings and lists under indexing
s = "cat"
try:
    s[0] = "b"              # strings are immutable
except TypeError as e:
    print("s[0] = 'b' : TypeError:", e)

letters = ["c", "a", "t"]
letters[0] = "b"            # lists are mutable
print("letters[0] = 'b':", letters)

print("'b' + s[1:] :", "b" + s[1:])   # 'bat' from 'cat'
