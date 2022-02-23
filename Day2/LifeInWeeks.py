# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Change age into a number
age_as_int = int(age)

# Calculate number of years left
year_remaining = 90 - age_as_int

# Calculate number of Days left
days_remaining = year_remaining * 365

# Calculate number of weeks left
weeks_remaining = year_remaining * 52

# Calculate number of Months left
months_remaining = year_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
