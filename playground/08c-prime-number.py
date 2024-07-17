# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# Create prime_checker function
def prime_checker(number):
  is_prime = True
  for i in range(2,number):     # start from 2, ... 
    if number%i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

# Input a number
n = int(input("Input the number that you want to check: ")) 
prime_checker(number=n)