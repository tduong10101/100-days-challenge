import turtle as t
from random import random, randint
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255) # pylint: disable=no-member

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)    
screen = t.Screen()
screen.exitonclick()