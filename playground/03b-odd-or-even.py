# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

# Which number do you want to check?
number = int(input())

# If the number can be divided by 2 with 0 remainder.
if number%2 == 0:
  print("This is an even number.")
  
# Otherwise (number cannot be divided by 2 with 0 remainder).
else:
  print("This is an odd number.")