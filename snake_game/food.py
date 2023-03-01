import random
from turtle import Turtle




class Food(Turtle):
    """The Food object"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.up()
        self.goto((random.randint(-280, 280), random.randint(-280, 280)))
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")

    def eaten(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)