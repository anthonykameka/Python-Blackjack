import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tony = Player()
cars = CarManager()
score = Scoreboard()
screen.update()
screen.listen()
screen.onkey(tony.move_up,"Up")


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    ## detect collision with cars

    for car in cars.all_cars:
        if car.distance(tony)<20:
            game_is_on = False
            score.game_over()

    ## detect completion

    if tony.ycor() > 290:
        tony.level_up()
        score.level_up()
        cars.level_up(score.level)


