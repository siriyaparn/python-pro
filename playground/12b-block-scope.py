# There is no Block Scope in Python

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]  
print(new_enemy)            

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]  # new_enemy is in an if block, so if you want to print
    print(new_enemy)            # print within the boundary of this function
#print(new_enemy)               # <- cannot print here, is you create a function

# The important thing
# If you create a variable within a function, then it is only available within hat function
# If you create a variable within an if block, or a while loop, or for loop, or anythind that has the indentation and colon,
# then that does not count as reating separate local scope.