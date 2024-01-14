from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("Sienna")

i = 0
while i < 4:
    tim.forward(100)
    tim.right(90)

    i += 1

i = 0
while i < 15:
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    i += 1

for sides in range(3, 11):
    tim.color(random.choice(["red", "black", "green", "blue", "brown", "yellow", "orange"]))
    walk = 0
    while walk < sides:
        tim.forward(100)
        tim.right(360 / sides)
        walk += 1

screen = Screen()
screen.exitonclick()
