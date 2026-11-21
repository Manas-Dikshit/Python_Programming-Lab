# 1. Trace string indexing: PYTHON
s = "PYTHON"
print("s[0] :", s[0])
print("s[3] :", s[3])
print("s[-1]:", s[-1])
print("s[-3]:", s[-3])

try:
    print(s[6])            # out of range: valid indexes are 0..5
except IndexError as e:
    print("s[6] : IndexError:", e)
