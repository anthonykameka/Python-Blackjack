from turtle import Turtle

STARTING_SCORE = 0
class Scoreboard(Turtle):
    """Scoreboard"""


    def __init__(self):
        super().__init__()
        self.score = 0
        self.up()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 12, "normal"))
        self.hideturtle()

    def point(self):

        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 12, "normal"))

    def game_over(self):


        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Courier", 19, "normal"))
        self.score = 0