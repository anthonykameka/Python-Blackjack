from turtle import Turtle

STARTING_SCORE = 0
class Scoreboard(Turtle):
    """Scoreboard"""


    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.up()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 12, "normal"))
        self.hideturtle()

    def update(self):

        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 12, "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def point(self):
        self.score += 1
        self.update()

    # def game_over(self):
    #
    #
    #     self.goto(0,0)
    #     self.write(f"Game Over", align="center", font=("Courier", 19, "normal"))
    #     self.score = 0