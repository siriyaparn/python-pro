# Using Reeborg's World 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Create turn right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Find the wall first
while front_is_clear():
    move()
turn_left()

# Find the exit
while not at_goal():
    if right_is_clear():    # Follow along the right edge
        turn_right()    
        move()
    elif wall_in_front:     # If there is wall in front -> turn left
        turn_left()
    else:
        move()              # Else move