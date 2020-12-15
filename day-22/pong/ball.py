from turtle import Turtle
from math import ceil
RIGHT_ANGLE = 90
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.reset_speed()
        self.x_move=10
        self.y_move=10
        
    def move(self):
        self.setpos(self.xcor()+self.x_move,self.ycor()+self.y_move)
    
    def bounce_y(self):
        self.y_move *=-1
        
    def bounce_x(self):
        self.x_move *=-1
        self.move_speed*=.9
        
    def ball_reset(self):
        self.setpos(0,0)
        self.reset_speed()
        self.bounce_x()
        
    def reset_speed(self):
        self.move_speed=.1