programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."
                          }

# Retrieve items in dictionary
print(programming_dictionary["Bug"])

# Add new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary) 
## output:
# {'Bug': 'An error in a program that prevents the program from running as expected.', 
# 'Function': 'A piece of code that you can easily call over and over again.', 
# 'Loop': 'The action of doing something over and over again.'}

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)
## output: {}

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)
## output:
# {'Bug': 'A moth in your computer.', 
# 'Function': 'A piece of code that you can easily call over and over again.', 
# 'Loop': 'The action of doing something over and over again.'}

# Loop through a dictionary
for key in programming_dictionary:
    print(key)                              # Print only keys
    print(programming_dictionary[key])      # Print values