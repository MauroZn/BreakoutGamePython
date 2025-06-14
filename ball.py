from turtle import Turtle
import random

STARTING_POSITION = (0, -229)
MOVE_DISTANCE = 20

class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("blue")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.has_run = False

    def start_ball(self):
        if not self.has_run:
            self.setheading(random.choice([45, 135]))
            self.has_run = True
        self.forward(MOVE_DISTANCE)

    def bounce_up(self):
        new_heading = (360 - self.heading()) % 360
        self.setheading(new_heading)

    def bounce_down(self):
        new_heading = (360 - self.heading()) % 360
        self.setheading(new_heading)

    def bounce_right(self):
        new_heading = (180 - self.heading()) % 360
        self.setheading(new_heading)

    def bounce_left(self):
        new_heading = (180 - self.heading()) % 360
        self.setheading(new_heading)
