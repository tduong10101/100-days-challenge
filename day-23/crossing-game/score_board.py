from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 32, "normal")
class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()        
        self.setpos(-210,280)
        self.hideturtle()
        self.level = 1
        self.write_score()
        
    def increase_level(self):
        self.level += 1
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.write(f"Level {self.level}",False, align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.setpos(0,0)
        self.write(f"GAME OVER",False, align=ALIGNMENT, font=GAME_OVER_FONT)