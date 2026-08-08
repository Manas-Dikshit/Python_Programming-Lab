# Practical Activity 1: To create variables of different data types.
name = "Rahul"
age = 20
cgpa = 8.75
is_student = True
print(name)
print(age)
print(cgpa)
print(is_student)

# Practical Activity 2: To understand valid and invalid variable names.
student_name = "Amit"
student1 = 101
_total = 500
print(student_name)
print(student1)
print(_total)

# Practical Activity 3: To assign values to variables.
x = 50
y = 25
print("Value of x =", x)
print("Value of y =", y)

# Practical Activity 4: To understand dynamic typing.
x = 10
print(x)
x = 15.5
print(x)
x = "Python"
print(x)

# Practical Activity 5: To assign one value to multiple variables.
a = b = c = 100
print(a)
print(b)
print(c)

# Practical Activity 6: To assign different values in one statement.
name, age, city = "Rahul", 20, "Sambalpur"
print(name)
print(age)
print(city)

# Practical Activity 7: To identify data types.
a = 50
b = 5.5
c = "Python"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Practical Activity 8: To update a variable.
salary = 25000
print("Old Salary =", salary)
salary = 30000
print("New Salary =", salary)

# Student Activity: Increase the salary by 5,000.
salary = salary + 5000
print("Updated Salary =", salary)

# Practical Activity 9: To understand local scope.
def student():
    name = "Rahul"
    print(name)

student()

# Practical Activity 10: To understand global scope.
college = "SUIIT"

def display():
    print(college)

display()
