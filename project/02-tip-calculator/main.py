# Create tip calculator
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to spilt the bill? "))

# Calculate tip
cal_tip = (total_bill * (1+tip/100)) / people
# answer = round(cal_tip, 2)
answer = "{:.2f}".format(cal_tip)
print(f"Each person should pay: ${answer}")