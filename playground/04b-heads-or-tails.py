# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# To practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".
# e.g. 1 means Heads 0 means Tails

import random

random_side = random.randint(0, 1) 
# print(random_side)

if random_side == 1:
  print("Heads")
else:
  print("Tails")