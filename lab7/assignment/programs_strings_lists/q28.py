# 28. Find palindromes after casefolding and removing whitespace
items = ["Level", "Python", "Never odd or even", "Radar"]
results = []

for s in items:
    normalized = "".join(s.casefold().split())
    if normalized == normalized[::-1]:
        results.append(s)

print(results)
