# Basic Operations in Python

# Print
print("Hello World")
# Variables
# Variable Namings: case - sensitive, letter(a-z), underscore, number(0-9)
x = 5
y = "Automation"
print(x)
print(y)

# Concatenation operation '+'
print("Hello " + y)

x = 10
y = 20

print(x + y)

# Syntax - Semicolons, indentations
if 10 > 5:
    print("10 is greater than 5")


# Functions - arguments
def sum(a, b):
    print(a + b)


x = sum(20, 30)

# Comments in Python

# Numbers - integers, floats, complex numbers
x = 5
y = 2.6
z = 7j

# Printing date type
print(type(x))
print(type(y))
print(type(z))

# Casting
x = int(2)  # 2
y = int(2.5)
z = float(1)
p = str(10)

# String operations - Indexing of Characters, length of string, Covert to Lower & Upper Case, Strip, replace, Split
x = "Hello World.."
print(x[3])
print(len(x))
print(x.lower())
print(x.upper())
print(x.strip())
print(x.replace("e", "a"))
print(x.split("W"))

# Input
print("Enter your name: ")
x = input()
print("Hello, " + x)

