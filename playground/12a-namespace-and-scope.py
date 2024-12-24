# Modifying Global Scope
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

# Local scope is within the function, you can use it only inside function
increase_enemies()
## output: enemies inside function: 2

# Global scope
print(f"enemies inside function: {enemies}")
##  enemies inside function: 1

# Global scope can be call within a function
player_health = 10
def drink_potion():
    potion_strenth = 2
    print(player_health)
## Call a drink_potion() function
drink_potion()
## output = 10