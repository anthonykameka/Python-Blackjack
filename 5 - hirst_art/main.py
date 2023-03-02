## Used to generate list of rgb colors

import colorgram

# rgb_colors = []
# colors = colorgram.extract('image2.jpg', 50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen
import random

tony = Turtle()


color_list = [(191, 164, 139), (208, 195, 183), (143, 90, 67), (72, 108, 128), (203, 192, 177), (150, 68, 80), (137, 166, 153), (69, 111, 89), (184, 90, 100), (128, 157, 165), (188, 99, 88), (179, 138, 146), (153, 142, 70), (77, 152, 119), (110, 45, 51), (63, 50, 57), (58, 55, 49), (209, 185, 177), (54, 54, 61), (92, 142, 155), (35, 69, 41), (120, 120, 144), (113, 46, 43), (45, 76, 51), (71, 64, 53), (57, 59, 77), (209, 193, 196), (207, 181, 184), (192, 199, 193), (185, 196, 186), (195, 198, 203), (42, 73, 80), (175, 197, 200), (190, 190, 196)]

my_screen = Screen()
my_screen.colormode(255)

def next_row_from_right():
    tony.up()
    tony.left(90)
    tony.forward(50)
    tony.left(90)

def next_row_from_left():
    tony.up()
    tony.right(90)
    tony.forward(50)
    tony.right(90)
def paint():
    tony.up()
    tony.goto(-250, -250)
    for _ in range (5):

        draw_row()
        next_row_from_right()
        draw_row()
        next_row_from_left()

def draw_circle():
    tony.color(random.choice(color_list))
    tony.begin_fill()
    tony.circle(20)
    tony.end_fill()
def draw_row():
    for _ in range(9):
        tony.dot(20, random.choice(color_list))
        tony.forward(50)
    tony.dot(20, random.choice(color_list))
    tony.pendown
    pass

paint()
tony.hideturtle()


#
my_screen.setup(600, 600)
#
my_screen.exitonclick()

