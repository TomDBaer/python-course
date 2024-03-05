from turtle import Turtle, Screen
import colorgram
from random import choice, randint

tim = Turtle()
screen = Screen()
# tim.shape("turtle")
colors = colorgram.extract('kirara.png', 30)

# color mode
tim.screen.colormode(255)
tim.penup()


def generated_color():
    color = colors[randint(0, len(colors) - 1)]
    return color.rgb


tim_y = 0
for _ in range(10):
    tim_y += 50
    for _ in range(10):
        tim.dot(20, generated_color())
        tim.forward(50)
    tim.teleport(0, tim_y)















screen.exitonclick()