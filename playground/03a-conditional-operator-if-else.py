# If and else statements
# If the person who's trying to purchase a ticket is not over 120 centimeters,then they can't ride on the rollercoaster.
# But if their height is greater than 120 centimeters, then they can ride.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")