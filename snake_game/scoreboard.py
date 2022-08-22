from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
POSITION = (0, 275)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(POSITION)
        self.color("white")

        self.score = 0
        self.write(f"Score = {self.score}", move = False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
    def add_point(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", move = False, align=ALIGNMENT, font=FONT)


