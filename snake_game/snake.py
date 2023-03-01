from turtle import Turtle
import time
MOVE_DISTANCE = 20
STARTING_POS = [(0,0), (-20, 0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """The Snake"""



    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
            for pos in STARTING_POS:
                self.add_part(pos)

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)

        self.snake_parts[0].forward(MOVE_DISTANCE)
        # self.snake_parts[0].left(90)

    def up(self):
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(UP)

    def down(self):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)

    def left(self):
        if self.snake_parts[0].heading() != RIGHT:
         self.snake_parts[0].setheading(LEFT)

    def right(self):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)


    def add_part(self, position):
        part = Turtle("square")
        part.color("green")
        part.up()
        part.goto(position)
        self.snake_parts.append(part)

    def ate(self):
        #snake eats - extend body
        last = self.snake_parts[-1]
        self.add_part(last.pos())

