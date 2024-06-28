# Multiple if-else
# If the person who's trying to purchase a ticket is not over 120 centimeters,then they can't ride on the rollercoaster.
# But if their height is greater than 120 centimeters, then they can ride.

# If you're less than 12 years old, you pay $5.
# If you're between 12 and 18 you pay $7.
# If you're over 18 then you pay the full adult price, which is $12.

# Ask if they want a photo, if they want, charge an extra $3.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want to a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")