# 27. Count characters by category in one input line
text = input("Enter a line: ")

counts = [0, 0, 0, 0]   # alphabetic, decimal digits, whitespace, other
for ch in text:
    if ch.isalpha():
        counts[0] += 1
    elif ch.isdecimal():
        counts[1] += 1
    elif ch.isspace():
        counts[2] += 1
    else:
        counts[3] += 1

print(counts)           # "Lab 2!" -> [3, 1, 1, 1]
