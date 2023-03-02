from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("AK's Pong Game")

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
screen.update()

screen.listen()



screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.075)

    ## DETECT COLLISION WITH WALL

    if ball.ycor() > 280 or ball.ycor() < -280:
        #get ball to bounce if hit Y
        ball.bounce_y()

    ## DETECT COLLISION WITH PADDLE

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        print("went past right")
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        print("went past left")
        ball.reset()
        score.r_point()







screen.exitonclick()