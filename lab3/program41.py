# Calculate the Body Mass Index (BMI).
weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in meters): "))

bmi = weight / height ** 2

print("BMI =", round(bmi, 2))
