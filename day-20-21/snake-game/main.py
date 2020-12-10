from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move_fwd()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_body(1)
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Dectect collision with tail
    
    for unit in snake.snake_body[1:]:
        if snake.head.distance(unit) < 10:
            game_is_on = False
            scoreboard.game_over()
            
screen.exitonclick()
