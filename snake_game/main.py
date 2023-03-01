from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anthony's Snake Game")
screen.tracer(0)
screen.listen()
stony = Snake() ## name of snake
snack = Food()
scoreboard = Scoreboard()


screen.update()
screen.onkey(stony.up,"Up")
screen.onkey(stony.down, "Down")
screen.onkey(stony.left, "Left")
screen.onkey(stony.right,"Right")


playing = True
while playing:
    screen.update()

    time.sleep(0.1)
    stony.move()

    ## Detect collision with food

    if stony.head.distance(snack) < 15:
        print("eating food... yum")
        snack.eaten()
        stony.ate()
        scoreboard.point()

    ## Detect collision with wall

    if stony.head.xcor() > 280 or stony.head.xcor() < -280 or stony.head.ycor() > 280 or stony.head.ycor() < -280:
        scoreboard.game_over()
        playing = False


    ## Detect collision with tail
    # if head collides with any body part
    for part in stony.snake_parts[1:]:

        if part.distance(stony.head)<10:
            scoreboard.game_over()
            playing = False















screen.exitonclick()