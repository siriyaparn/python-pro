# Create list of dirty dozen
# As you can see, some of these are fruits like strawberries, apples, and the other ones are vegetables.
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches",
#                "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Create 2 lists, fruits and vegetables
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Create nested lists
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
## output: [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]
print(dirty_dozen[1][1])
# output: Kale

print(dirty_dozen[0][1])
# output: Nectarines