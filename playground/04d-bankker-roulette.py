# write a program that is going to select a random name from a list of names.
# And the person selected will have to pay for everyone's food bill.

# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
## output: ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe', .......]

import random
# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, len(names)-1)

# Choose and print a random name.
print(names[random_choice] + " is going to buy the meal today!")