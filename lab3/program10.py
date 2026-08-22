# Display a student's mark sheet using formatted output.
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))

m1 = float(input("Enter marks in Python: "))
m2 = float(input("Enter marks in Maths: "))
m3 = float(input("Enter marks in Physics: "))
m4 = float(input("Enter marks in Chemistry: "))
m5 = float(input("Enter marks in English: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

print("\n" + "=" * 40)
print(f"{'MARK SHEET':^40}")
print("=" * 40)
print(f"{'Name':<20}: {name}")
print(f"{'Roll No.':<20}: {roll}")
print("-" * 40)
print(f"{'Subject':<25}{'Marks':>10}")
print("-" * 40)
print(f"{'Python':<25}{m1:>10.2f}")
print(f"{'Maths':<25}{m2:>10.2f}")
print(f"{'Physics':<25}{m3:>10.2f}")
print(f"{'Chemistry':<25}{m4:>10.2f}")
print(f"{'English':<25}{m5:>10.2f}")
print("-" * 40)
print(f"{'Total':<25}{total:>10.2f}")
print(f"{'Percentage':<25}{percentage:>10.2f}%")
print("=" * 40)
