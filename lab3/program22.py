# Accept student details from the user and display them in a formatted manner.
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
branch = input("Enter branch: ")
semester = int(input("Enter semester: "))
cgpa = float(input("Enter CGPA: "))

print("\n========== STUDENT DETAILS ==========")
print(f"Name      : {name}")
print(f"Roll No.  : {roll}")
print(f"Branch    : {branch}")
print(f"Semester  : {semester}")
print(f"CGPA      : {cgpa:.2f}")
print("=====================================")
