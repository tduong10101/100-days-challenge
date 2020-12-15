from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
import random

UP = 90
DOWN = 270
TOP = 240
BOT = -240
TOP_BD = 280
BOT_BD = -280
RIGHT_BD = 320
LEFT_BD = -320
OUT=380

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()


r_paddle = Paddle()
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
direction = UP
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # if r_paddle.ycor() >= TOP:
    #     direction=DOWN
    # elif r_paddle.ycor() <= BOT:
    #     direction=UP

    # top/bot collision
    if ball.ycor() >= TOP_BD:
        ball.bounce_y()
    elif ball.ycor() <= BOT_BD:
        ball.bounce_y()
    # paddle collision
    if (ball.distance(r_paddle) < 50 and ball.xcor() > RIGHT_BD) or (ball.distance(l_paddle) < 50 and ball.xcor() < LEFT_BD):
        ball.bounce_x()
        
    # ball goes out
    if ball.xcor() > OUT:
        ball.ball_reset()
        scoreboard.increase_l_score()
    elif ball.xcor() < -OUT:
        ball.ball_reset()
        scoreboard.increase_r_score()
    # r_paddle.auto_move(direction)


screen.exitonclick()
