from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


tim = Turtle()
tim.goto(x=-230, y=-100)

screen.exitonclick()