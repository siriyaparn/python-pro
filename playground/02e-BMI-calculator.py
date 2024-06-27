# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
# NOTE: You should convert the bmi to a whole number and print out a whole number.

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()

# Check data type
print(type(height))
print(type(weight))

# Convent height from str to float
height_float = float(height)
# Convent weight from str to int
weight_int = int(weight)

# Calculate BMI
BMI = weight_int/(height_float**2)
print(int(BMI))     # round number