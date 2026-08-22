# Display an employee salary slip using f-string formatting.
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
basic = float(input("Enter basic salary: "))
hra = basic * 0.20
da = basic * 0.10
pf = basic * 0.12
net_salary = basic + hra + da - pf

print("\n" + "=" * 35)
print(f"{'SALARY SLIP':^35}")
print("=" * 35)
print(f"{'Employee Name':<20}: {name}")
print(f"{'Employee ID':<20}: {emp_id}")
print("-" * 35)
print(f"{'Basic Salary':<20}: Rs.{basic:>10.2f}")
print(f"{'HRA (20%)':<20}: Rs.{hra:>10.2f}")
print(f"{'DA (10%)':<20}: Rs.{da:>10.2f}")
print(f"{'PF (12%)':<20}: Rs.{pf:>10.2f}")
print("-" * 35)
print(f"{'Net Salary':<20}: Rs.{net_salary:>10.2f}")
print("=" * 35)
