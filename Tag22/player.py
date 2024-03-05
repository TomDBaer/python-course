from turtle import Turtle


class Player(Turtle):
    def __init__(self, x_pos=0, y_pos=0):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x_pos, y_pos)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(y=new_y, x=self.xcor())

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(y=new_y, x=self.xcor())
