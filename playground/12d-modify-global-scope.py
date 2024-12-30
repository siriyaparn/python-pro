# Modify global scope 
enemies = 1

def increase_enemies():
    # To create a global variable inside a function, you can use the global keyword.
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies() # Local scope
print(f"enemies inside function: {enemies}") # Global scope

##################################### Another way ###################################
def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies inside function: {enemies}")