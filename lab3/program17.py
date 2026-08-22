# Display a number in binary, octal and hexadecimal forms.
number = int(input("Enter an integer: "))

print("Binary     :", bin(number))
print("Octal      :", oct(number))
print("Hexadecimal:", hex(number))

print("\nUsing format():")
print(format(number, 'b'), format(number, 'o'), format(number, 'x'))
