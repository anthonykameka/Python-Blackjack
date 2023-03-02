from turtle import Turtle
STARTING_POS = (350, 0)



class Paddle(Turtle):
    """Paddle to Pong With"""

    def __init__(self, pos):
        super().__init__()
        self.create_paddle(pos)




    def create_paddle(self, pos):
        self.shape("square")
        self.color("blue")
        self.up()
        self.speed("fastest")
        self.goto(pos)

        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)





