# 16. Check identifiers, ASCII and printable characters
import keyword

for s in ["student_1", "1student", "class", "café", "A\nB"]:
    print(f"{s!r:12} isidentifier={s.isidentifier():5} "
          f"isascii={s.isascii():5} isprintable={s.isprintable():5}")

print("keyword.iskeyword('class'):", keyword.iskeyword("class"))
# "class" is a reserved Python keyword, so it cannot be a variable name.
