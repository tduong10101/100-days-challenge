from turtle import Turtle, Screen
from random import random
tim = Turtle()
tim.shape("turtle")
tim.color("red")

for i in range(3,15):
    angle = 360 / i
    
    tim.color(random(),random(),random())
    for j in range (i):
        tim.right(angle)
        tim.forward(100)
    
screen = Screen()
screen.exitonclick()