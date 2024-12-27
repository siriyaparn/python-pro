# Modify global scope 
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

# Local scope
increase_enemies()

# Global scope
print(f"enemies inside function: {enemies}")