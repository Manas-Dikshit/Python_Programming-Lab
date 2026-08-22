# Calculate Simple Interest accepting principal, rate and time from user.
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)
print("Total Amount    =", principal + simple_interest)
