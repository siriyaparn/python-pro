# Modify global scope 
enemies = 1

def increase_enemies():
    # To create a global variable inside a function, you can use the global keyword.
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

# Local scope
increase_enemies()

# Global scope
print(f"enemies inside function: {enemies}")