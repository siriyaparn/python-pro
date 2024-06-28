# Nested if-else
# If the person who's trying to purchase a ticket is not over 120 centimeters,then they can't ride on the rollercoaster.
# But if their height is greater than 120 centimeters, then they can ride.

# If you're less than 12 years old, you pay $5.
# If you're between 12 and 18 you pay $7.
# If you're over 18 then you pay the full adult price, which is $12.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")