from turtle import Turtle

class CrossingTurtle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.restart()
        
    def move(self):
        self.forward(40)
        
    def restart(self):
        self.setpos(0,-280)