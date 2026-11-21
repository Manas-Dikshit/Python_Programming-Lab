# 14. Classify Unicode text with the numeric and character predicates
samples = ["123", "²", "Ⅻ", "A1", "A", " ", ""]
for s in samples:
    print(f"{s!r:6} isdecimal={s.isdecimal():5} isdigit={s.isdigit():5} "
          f"isnumeric={s.isnumeric():5} isalnum={s.isalnum():5} "
          f"isalpha={s.isalpha():5} isspace={s.isspace():5}")
# isdecimal < isdigit < isnumeric: "123" passes all three, "²" passes digit/numeric,
# "Ⅻ" passes only numeric.
