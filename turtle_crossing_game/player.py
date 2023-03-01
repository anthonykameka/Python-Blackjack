from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """User player"""

    def __init__(self):
        super().__init__()
        self.up()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move_up(self):
        self.forward(MOVE_DISTANCE)


    def level_up(self):
        self.goto(STARTING_POSITION)
