# Create treasure map
# created a Treasure Map by creating three lists which called line1, line2, and line3, 
# and combined them into a nested list by using the code line four
# Your job is to take an input in a similar format to how you see maps are formatted,
# where we can take a letter and a number and then use those letters and numbers to access a particular location in our list
# and convert the entry into an X to mark a spot on our map where we've buried our treasure.

## Map location
#      A    B    C
#  1 ["⬜️","️⬜️","️⬜️"]
#  2 ["⬜️","⬜️","️⬜️"]
#  3 ["⬜️️","⬜️️","⬜️️"]


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? e.g. A2, C1, .. ") # Where do you want to put the treasure?

## Method 1
# Takes the first character to be letter
letter = position[0].lower()
# Create condition to change index
if letter == "a":
  letter_position = 0
elif letter == "b":
  letter_position = 1
else:
  letter_position = 2

# Takes the second character to be letter
number = position[1].lower()
# Create condition to change index
if number == "1":
  number_position = 0
elif number == "2":
  number_position = 1
else:
  number_position = 2

# Print treasure location
map[number_position][letter_position] = "X"

print(f"{line1}\n{line2}\n{line3}")

## Method 2
letter = position[0].lower()

# Play with index
abc = ["a","b","c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1

# Print treasure location
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")