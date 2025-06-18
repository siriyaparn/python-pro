from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)

# Challenge 1: Draw a squre
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

# Challenge 2: Draw a dashed line 
import turtle as t
tim = t.Turtle()

for _ in range(10):
    tim.forward(10)
    tim.penup
    tim.forward(10)
    tim.pendown

# Challenge 3: Drawing different shape
import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchild", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(nem_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()