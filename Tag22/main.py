"""
Klassen: Spieler, Punktestand (Spielfeld), Ball
Struktur: Bewegung der Spieler, CPU bewegung, Ball bewegung, Kollisionen (mit spieler, mit wand)

"""

from turtle import Screen
from player import Player
from ball import Ball
from counter import Counter
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pog")
screen.tracer(0)

# test new player
player1 = Player(x_pos=350)
player2 = Player(x_pos=-350)
ball = Ball()
counter = Counter()

screen.listen()
screen.onkeypress(key="w", fun=player1.move_up)
screen.onkeypress(key="s", fun=player1.move_down)

game_is_on = True
while game_is_on:
    # sorgt dafür das sich der ball langsamer bewegt
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall | top,bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right player
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if player 1 didn't hit
    if ball.xcor() > 380:
        ball.reset_position()
        counter.l_point()

    # Detect if player 2 didn't hit
    if ball.xcor() < -380:
        ball.reset_position()
        counter.r_point()

# screen exit
screen.exitonclick()
