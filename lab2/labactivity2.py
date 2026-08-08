# Local and Global Variables

# Global Variable (accessible everywhere)
x = 50
print("Global x =", x)

def show():
    # Local Variable (accessible only inside this function)
    x = 10
    print("Local x =", x)

show()
print("Global x =", x)

# Using 'global' keyword to modify the global variable inside a function
def change():
    global x
    x = 100
    print("Changed global x =", x)

change()
print("Global x after change =", x)

# Example showing local variable does not affect global variable
y = 5

def add():
    y = 10
    y = y + 2
    print("Local y =", y)

add()
print("Global y =", y)
