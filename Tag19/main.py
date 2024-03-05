import turtle
from turtle import Turtle, Screen
from random import randint

# Turtle klasse erstellen
class MyTurtle:
    def __init__(self):
        color = "black"


is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Gacha", prompt="Which turtle will win: ")
my_y = -100

all_turtles = []

for c in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(c)
    new_turtle.goto(x=-230, y=my_y)
    my_y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        random_distance = randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
