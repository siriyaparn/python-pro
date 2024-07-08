# Using Reeborg's World 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# Create turn right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Create jump function
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Find the goal
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()