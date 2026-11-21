# 13. Compare partition() and rpartition()
for s in ("a=b=c", "abc"):
    print(s, "partition    :", s.partition("="))
    print(s, "rpartition   :", s.rpartition("="))
# Three fields: part before the separator, the separator itself, part after it.
# With no separator the first field is the whole string and the other two are ''.
