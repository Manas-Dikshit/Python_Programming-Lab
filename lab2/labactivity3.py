import sys


num1, num2 = map(int, input("Enter two numbers: ").split())
print("Sum:", num1 + num2)
#we also can do it with map function
n1, n2 = map(int, input("Enter two numbers: ").split())
print("Sum:", n1 + n2)

#print output function parameters
name = input("Enter your name: ")
print("Hello,", name)
print("Hello,", name, "Welcome to SUIIT")
print("Hello,", name, "Welcome to SUIIT", sep=" - ")
print("Hello,", name, "Welcome to SUIIT", end="!!!\n")
print("Hello,", name, "Welcome to SUIIT", sep=" - ", end="!!!\n")
print("Hello,", name, "Welcome to SUIIT", sep=" - ", end="!!!\n", flush=True)
print("Hello,", name, "Welcome to SUIIT", sep=" - ", end="!!!\n", flush=True, file=sys.stdout)