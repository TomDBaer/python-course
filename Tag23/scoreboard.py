from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.setpos(x=-290, y=260)
        self.write(f"Level: {self.score}", move=False, align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", move=False, align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
