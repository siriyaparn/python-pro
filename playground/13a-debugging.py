def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")

my_function()

# Describe the problem
# What is the for loop doing?
## Ans: Loop through all the numbers between 1 and 20, and then once that number reaches 20, it's supposed to print "You got it"

# When is the function meant to print "You got it"?
## Ans: When it reaches 20

# What are your assumptions about the vaule of it?
## Ans: When we write 1, 20, it actually goes from 1 all the way up to 19, but not including 20. The problem here is that i actually never reaches 20, so this assumption is completely false.