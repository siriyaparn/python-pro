#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_easy = ""
for char in range(1, nr_letters+1):
    password_easy += random.choice(letters)
    # print(password_easy)

for sym in range(1, nr_symbols+1):
    password_easy += random.choice(symbols)
    # print(password_easy)

for num in range(1, nr_numbers+1):
    password_easy += random.choice(numbers)
    # print(password_easy)

print(f"Here is your password (easy_version): {password_easy}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
    # print(password_list)

for sym in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))
    # print(password_list)

for num in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))
    # print(password_list)
# print(password_list)

# Randomize characters in password_list
random.shuffle(password_list)
# print(password_list)

# Convert list to string
password_hard = ""
for character in password_list:
    password_hard += character

# Print output
print(f"Here is your password (hard version): {password_hard}")