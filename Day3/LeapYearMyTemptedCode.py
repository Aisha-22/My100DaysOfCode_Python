# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# if year % 2000 == 4:
#     print("on every year that is evenly divisible by 4")
# elif year % 2000 == 100:
#     print("**except** every year that is evenly divisible by 100")
# else:
#     print("**unless** the year is also evenly divisible by 400")
if year % 4 == 0:
    print("Leap year.")
elif year % 100 == 0:
    print("Not leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
