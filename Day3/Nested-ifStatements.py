print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age"))
    if age <= 18:
        print("Please pay R7 Ticket")
    else:
        print("Please pay R12 Ticket")
else:
    print("Sorry - Wait till your height is 120 or over")
