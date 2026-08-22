# Calculate the Electricity Bill from units consumed and cost per unit.
units = float(input("Enter number of units consumed: "))
cost_per_unit = float(input("Enter cost per unit: "))

bill = units * cost_per_unit

print("Total Electricity Bill = Rs.", bill)
