# Accept three integers in a single line using map() and display their sum and average.
a, b, c = map(int, input("Enter three integers separated by space: ").split())

total = a + b + c
average = total / 3

print("Sum     =", total)
print("Average =", average)
