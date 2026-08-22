# Calculate the net amount after applying a 10% discount.
price = float(input("Enter product price: "))

discount = price * 0.10
net_amount = price - discount

print(f"Discount (10%) : Rs.{discount:.2f}")
print(f"Net Amount     : Rs.{net_amount:.2f}")
