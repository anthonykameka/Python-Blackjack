from turtle import Turtle
FONT = ("Courier", 24, "normal")
STARTING_LEVEL = 1

class Scoreboard(Turtle):

"""ScoreSheet"""
    def __init__(self):
        super().__init__()
        self.up()
        self.level = 1
        self.goto(-240, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.hideturtle()


    def level_up(self):

        self.level +=1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def game_over(self):

        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)


