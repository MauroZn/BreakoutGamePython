from turtle import Turtle
import random

COLORS = ["green", "lightgreen", "yellow", "orange", "red"]

BRICKS_POSITIONS = [(-210, 140), (-140, 140), (-70, 140), (0, 140), (70, 140), (140, 140), (210, 140),
                    (-210, 170), (-140, 170), (-70, 170), (0, 170), (70, 170), (140, 170), (210, 170),
                    (-210, 200), (-140, 200), (-70, 200), (0, 200), (70, 200), (140, 200), (210, 200),
                    (-210, 230), (-140, 230), (-70, 230), (0, 230), (70, 230), (140, 230), (210, 230),
                    (-210, 260), (-140, 260), (-70, 260), (0, 260), (70, 260), (140, 260), (210, 260)
]

class BricksManager:

    def __init__(self):
        self.all_bricks = []
        self.create_bricks()

    def create_bricks(self):
        n_bricks = 0
        c_number = 0
        for brick in BRICKS_POSITIONS:
            new_brick = Turtle("square")
            new_brick.shapesize(stretch_wid=1, stretch_len=3)
            new_brick.penup()
            n_bricks += 1
            if n_bricks == 8 or n_bricks == 15 or n_bricks == 22 or n_bricks == 29: c_number += 1
            new_brick.color(COLORS[c_number])
            new_brick.goto(brick)
            self.all_bricks.append(new_brick)
