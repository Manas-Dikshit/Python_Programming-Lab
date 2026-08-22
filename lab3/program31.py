# Accept marks of five subjects, calculate total marks and percentage.
total = 0
for i in range(1, 6):
    marks = float(input(f"Enter marks of subject {i}: "))
    total += marks

percentage = (total / 500) * 100

print("Total Marks =", total)
print("Percentage  =", percentage)
