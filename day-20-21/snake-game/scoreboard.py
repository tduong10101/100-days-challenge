from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(0, 260)
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.update()

    def update(self):
        self.write(f"Your score is: {self.score}",
                   False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
