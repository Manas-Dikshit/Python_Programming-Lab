# Calculate Gross Salary of an employee with HRA (20%) and DA (10%).
basic = float(input("Enter Basic Salary: "))

hra = basic * 0.20
da = basic * 0.10
gross_salary = basic + hra + da

print(f"Basic Salary : Rs.{basic:.2f}")
print(f"HRA (20%)    : Rs.{hra:.2f}")
print(f"DA (10%)     : Rs.{da:.2f}")
print(f"Gross Salary : Rs.{gross_salary:.2f}")
