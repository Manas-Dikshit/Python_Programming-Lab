# Create a formatted table containing Roll No., Name and Marks of three students.
students = [
    (101, "Rahul", 85),
    (102, "Priya", 92),
    (103, "Amit", 78),
]

print(f"{'Roll No.':<10}{'Name':<15}{'Marks':>8}")
print("-" * 33)
for roll, name, marks in students:
    print(f"{roll:<10}{name:<15}{marks:>8}")
