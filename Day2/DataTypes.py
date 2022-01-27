# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# Type checking and Type conversion

# This variable will take the fist digit at the position [0] of the two_digit_number through the input function from
# the user/users keyboard
first_digit = two_digit_number[0]

# This variable will take the second at the position [1] of the two_digit_number through the input function from
# # the user/users keyboard
second_digit = two_digit_number[1]

# These functions will calculate the numbers by adding the two_digit_number together and will be assigned to the
# variable 'result'
result = int(first_digit) + int(second_digit)

# This print function will print the result
print(result)

#  Aisha - Prac

name = "Aisha"

print(f"The letter at position 0 for Aisha = {name[0]}")
print(name[1])
print(name[2])
print(name[3])
print(name[4])
