from turtle import Turtle
import turtle as t
import random
COLOR = [(208, 159, 108), (223, 206, 117), (136, 173, 194), (215, 231, 240), (39, 107, 140), (137, 184, 147), (13, 52, 76), (219, 87, 63), (145, 80, 71), (70, 165, 119), (30, 129, 106), (125, 80, 96), (10, 58, 50), (55, 153, 180), (196, 
130, 144), (52, 33, 43), (129, 37, 49), (4, 111, 88), (207, 83, 101), (176, 206, 167), (230, 168, 182), (155, 152, 70), (145, 204, 233), (33, 64, 101), (13, 87, 105), (46, 30, 26), (184, 189, 204)]
t.colormode(255) # pylint: disable=no-member
class Car(Turtle):
    
    def __init__(self,xpos,ypos):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLOR))
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.setpos(xpos,ypos)
        
class Lane:
    
    def __init__(self,length,ypos,num_car):        
        self.max_x = int(length/2 + 30)
        self.min_x = int(-self.max_x)
        self.ypos = ypos
        self.car_list = [] 
        for _ in range(num_car):
            car_xpos = random.randint(self.min_x,self.max_x)
            
            self.car_list.append(Car(car_xpos,ypos))
            
    def move(self):
        for car in self.car_list:
            car.forward(-5)
            if car.xcor() <= self.min_x:
                car.setpos(self.max_x, self.ypos)
                
    def reset_lane(self):
        for car in self.car_list:
            car_xpos = random.randint(self.min_x,self.max_x)
            car.setpos(car_xpos,self.ypos)