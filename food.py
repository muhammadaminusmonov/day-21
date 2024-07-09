from turtle import Turtle
import random
from scoreboard import Scoreboard


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        position_x = random.randint(-280, 280)
        position_y = random.randint(-280, 280)
        self.goto(position_x, position_y)
