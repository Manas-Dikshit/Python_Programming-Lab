# Frozenset datatype: set that is IMMUTABLE (usable as dict key etc.)
skills = frozenset(["python", "java", "python"])

print("skills (duplicates removed) =", skills)
print("type(skills) :", type(skills))

langs = frozenset(["python", "c"])
print("langs =", langs)

print("skills | langs :", skills | langs)
print("skills & langs :", skills & langs)
print("skills - langs :", skills - langs)
print("'python' in skills :", "python" in skills)
print("len(skills) :", len(skills))

# skills.add("rust") would fail: frozenset has no add/discard
