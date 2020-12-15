from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(0, 260)
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        
        self.hideturtle()
        self.color("white")
        self.update()

    def update(self):        
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}",
                   False, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update()