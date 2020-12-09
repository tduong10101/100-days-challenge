from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:
    def __init__(self):
        self.snake_body = []
        self.body_unit = 20
        self.add_body(3)
        self.head = self.snake_body[0]

    def add_body(self,unit):
        for _ in range(unit):
            u = Turtle("square")
            u.color("green")
            u.penup()
            if len(self.snake_body) > 0:
                last_unit = self.snake_body[-1]
                x_pos = 0
                y_pos = 0
                if last_unit.heading() == 0:
                    x_pos -= self.body_unit
                elif last_unit.heading() == 90:
                    y_pos -= self.body_unit
                elif last_unit.heading() == 180:
                    x_pos += self.body_unit
                elif last_unit.heading() == 270:
                    y_pos += self.body_unit

                u.setpos(last_unit.xcor()+x_pos, last_unit.ycor()+y_pos)
            
            self.snake_body.append(u)
    
    def move_fwd(self):        
        for unit in range(len(self.snake_body)-1,0,-1):
            self.snake_body[unit].setpos(self.snake_body[unit-1].pos())
            self.snake_body[unit].setheading(self.snake_body[unit-1].heading())            
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.get_heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.get_heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def up(self):
        if self.get_heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.get_heading() != UP:
            self.head.setheading(DOWN)
        
    def get_heading(self):
        return self.head.heading()