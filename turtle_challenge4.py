from turtle import Turtle, Screen
import random

tim = Turtle()

# tim.shape("turtle")
tim.color("Sienna")
tim.speed(10)
# speed in range (0,10),0 is fastest, 10 is fast, 6 is normal

color = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown", "Gray", "Black", "Magenta", "Indigo",
         "Violet", "midnightBlue", "DarkSlateGray", "Maroon", "Orchid", "aqua", "Firebrick", "Chocolate", "DeepPink",
         "BlueViolet"]
direction = [90, 180, 270, 360]

i = 0
while True:
    tim.width(i)
    tim.color(random.choice(color))
    tim.forward(20)
    tim.setheading(random.choice(direction))
    # tim.right(random.choice(direction))
    i += 0.005

screen = Screen()

screen.exitonclick()
