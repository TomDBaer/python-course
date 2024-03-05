import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Init Screen
screen = Screen()

# screen setup
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snek")

# tracer / Animation an aus schalten
# wirft einen loop
screen.tracer(0)

# init snake
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # snake
    snake.move()

    # collision snake - food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.score_up()

    # Detect collision with wall
    if snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
        score.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    # old but functional
    # Detect collision with tail
    """
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    """
    # improved with slicing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()


# close on screen click
screen.exitonclick()
