from turtle import Screen, Turtle
import turtle as t
from crossing_turtle import CrossingTurtle
from score_board import ScoreBoard
from car import Car, Lane
import random
import time

FIRST_LANE_POS = -240
LAST_LANE_POS = 280
MAX_CAR = 5
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
MAX_X = 280
MIN_X = -280
LANE_SPACE = 40
sleep_time = 0.1

screen = Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()
game_is_on = True

turtle = CrossingTurtle()
current_lane = FIRST_LANE_POS
lanes = []
while current_lane < LAST_LANE_POS:
    num_car = random.randint(1,MAX_CAR)
    lane = Lane(SCREEN_WIDTH,current_lane,num_car)
    lanes.append(lane)
    
    current_lane += LANE_SPACE

score_board = ScoreBoard()

screen.onkey(fun=turtle.move, key="Up")

while game_is_on:
    
    time.sleep(sleep_time)
    if turtle.ycor() >= 290:
        score_board.increase_level()
        turtle.restart()
        sleep_time *=.8
        for lane in lanes:
            lane.reset_lane()

    for lane in lanes:
        lane.move()
        for car in lane.car_list:
            if turtle.distance(car) < 20:
                game_is_on = False                   
                    
    screen.update()

score_board.game_over()    
screen.exitonclick()