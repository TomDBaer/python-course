import turtle
from turtle import Screen, Turtle
import pandas

# Turtle setup
state = Turtle()
state.penup()
state.hideturtle()

# screen setup
screen = Screen()
screen.title("Some States")
screen.setup(width=725, height=491)
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')

# csv laden
data = pandas.read_csv('50_states.csv')

game_running = True
game_turn = 0
state_count = data['state'].count()

print(data.loc[data['state'] == 'Ohio'].x.item())

def answer_fun() -> str:
    return screen.textinput(title=f"{game_turn}/{state_count} States Correct", prompt="What state name?: ").title()


while game_running:
    answer = answer_fun()

    if any(data.state == answer):
        x_pos = data.loc[data['state'] == answer].x.item()
        # oder
        y_pos = data[data['state'] == answer].values[0][2]
        state.goto(x=x_pos, y=y_pos)
        state.write(answer)
        game_turn += 1
    else:
        game_running = False


