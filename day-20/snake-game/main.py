from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
    
snake = Snake()

game_is_on = True
while game_is_on:    
    screen.update()
    time.sleep(.1)
    snake.move_fwd()     
    screen.onkey(key = "Left", fun=snake.left)
    screen.onkey(key = "Right", fun=snake.right)    
    screen.onkey(key = "Up", fun=snake.up)
    screen.onkey(key = "Down", fun=snake.down) 


screen.exitonclick()
