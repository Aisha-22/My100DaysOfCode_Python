# If, ElIf and Else statements and Conditions

if 5 > 3:
    print("5 Is greater than 3")

num = 10

if num > 5:
    print("This is a positive number")

elif num == 10:
    print("num is 10")

else:
    print("This ia a negative number")

# ForLoop

num = [1, 2, 3, 4, 5]
sum = 10

for val in num:
    sum = sum + val
print("Total is ", sum)

fruits = ["Apple", "Orange", "Banana"]

for val in fruits:
    print(val)

else:
    print("No fruits left")

# While Loop

num = int(input("Enter number: "))
sum = 0
i = 1

while i < num:
    sum = sum + 1
    i = i + 1
print("Total is: ", sum)
