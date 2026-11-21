# 10. Validate prefixes and suffixes with if/elif/else
files = ["report.pdf", "draft_notes.txt", "draft_work.pdf"]
for name in files:
    if name.startswith("draft_") and name.endswith(".pdf"):
        label = "Draft PDF"
    elif name.endswith(".pdf"):
        label = "Other PDF"
    else:
        label = "Other file"
    print(name, "->", label)
