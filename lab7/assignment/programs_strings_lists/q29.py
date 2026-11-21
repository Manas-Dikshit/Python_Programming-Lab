# 29. Remove duplicate words, keeping the first lowercase occurrence
words = input("Enter words: ").split()
seen = []

for word in words:
    w = word.casefold()
    if w in seen:
        continue
    seen.append(w)

print(",".join(seen))   # "Red blue RED green" -> red,blue,green
