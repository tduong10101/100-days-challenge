import turtle as t
from random import random, randint
tim = t.Turtle()
tim.color("red")
tim.pensize(15)
tim.speed(0)
t.colormode(255) # pylint: disable=no-member

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r, g, b)

for i in range(200):
    tim.color(random_color())
    direction = 90 * randint(1,5)
    tim.right(direction)
    tim.forward(30)
    
screen = t.Screen()
screen.exitonclick()