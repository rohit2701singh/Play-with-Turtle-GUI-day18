from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
tim = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = r, g, b
    return random_color_tuple


tim.speed(0)
# # speed in range (0,10),0 is fastest, 10 is fast, 6 is normal
direction = [90, 180, 270, 360]

i = 0
while True:
    tim.width(i)
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(direction))
    # tim.right(random.choice(direction))
    i += 0.005

screen = Screen()
screen.exitonclick()
