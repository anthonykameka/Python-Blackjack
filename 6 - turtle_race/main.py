from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput("Welcome to TurtleRace (trademarked)", "select a color (r-o-y-g-b-i-v) use full color name")
print(user_choice)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
startingX = -220
startingY = -120
finishX = 250
paces = [5, 10, 15, 20, 25]
turtles = []
racing = True
for i in range(6):
    tony = Turtle(shape="turtle")
    tony.color(colors[i-1])
    tony.up()
    tony.goto(startingX, startingY + (i*50))
    turtles.append(tony)

while racing:
    for turtle in turtles:
        if turtle.xcor() > 250:
            racing = False
            winning_color = turtle.color()
            if winning_color == user_choice:
                print(f" Your choice, {winning_color} won - goodjob!")
            else:
                print(f" You lost! {winning_color} won - sorry")

        if random.randint(0,4) > 0:
            turtle.forward(random.choice(paces))
        else:
            turtle.backward(random.choice(paces))



screen.exitonclick()