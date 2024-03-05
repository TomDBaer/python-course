from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'bold')


def load_highscore() -> int:
    with open("score.txt") as file:
        highscore = file.read()
    return int(highscore)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = load_highscore()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 220)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def score_up(self):
        self.score += 1
        self.update_scoreboard()
