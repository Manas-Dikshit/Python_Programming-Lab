# 15. Check letter case predicates
for s in ["python", "PYTHON", "Python Lab", "123"]:
    print(f"{s!r:14} islower={s.islower():5} isupper={s.isupper():5} istitle={s.istitle():5}")
