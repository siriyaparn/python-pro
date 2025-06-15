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

screen = Screen()
screen.exitonclick()