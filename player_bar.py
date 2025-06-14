from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 30

class PlayerBar(Turtle):

    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color("gray")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(STARTING_POSITION)

    def right(self):
        if self.xcor() < 200:
            self.forward(MOVE_DISTANCE)

    def left(self):
        if self.xcor() > -220:
            self.backward(MOVE_DISTANCE)
