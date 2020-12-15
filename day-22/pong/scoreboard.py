from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()        
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.r_score=0
        self.l_score=0
        self.update()

    def update(self):
        self.setpos(-100, 200)
        self.write(f"{self.l_score}",
                   False, align=ALIGNMENT, font=FONT)
        self.setpos(100, 200)
        self.write(f"{self.r_score}",
                   False, align=ALIGNMENT, font=FONT)


    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update()
        
    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update()
