from turtle import Turtle
UP=90

class Paddle(Turtle):

    def __init__(self, pos=(350,0)):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(UP)
        self.shape("square")
        self.color("white")
        self.penup()
        self.setposition(pos)
        
        
    def go_up(self):
        self.sety(self.ycor()+30)
        
    def go_down(self):
        self.sety(self.ycor()-30)
        
    def auto_move(self, direction):
        self.setheading(direction)
        self.forward(20)
