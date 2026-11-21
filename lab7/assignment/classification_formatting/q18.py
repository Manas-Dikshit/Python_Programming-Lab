# 18. Format a marks record two ways
name = "Riya"
score = 87.5

print("{name} scored {score:.2f}".format(name=name, score=score))
values = {"name": name, "score": score}
print("{name} scored {score:.2f}".format_map(values))
