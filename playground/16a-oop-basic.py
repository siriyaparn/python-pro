from turtle import Turtle, Screen


# object = class
timmy = Turtle()        # Create object
print(timmy)
timmy.shape("turtle")   # Call methods
timmy.color("DarkSlateGray1")
timmy.forward(100)

# the screen represents the window in which this turtle is going to show up
my_screen = Screen()
print(my_screen.canvheight) # tab into attribute: object.attribute
my_screen.exitonclick()