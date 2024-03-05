from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
tim.shape("turtle")

# spirograph

# color mode
tim.screen.colormode(255)
# turn angle
turn = 20
# go fast
tim.speed(0)


def random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    return r, b, g


for _ in range(int(360/turn)):
    tim.color(random_color())
    tim.circle(100)
    tim.right(turn)














screen = Screen()
screen.exitonclick()