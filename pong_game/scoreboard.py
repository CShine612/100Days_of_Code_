from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(position)
        self.color("white")

        self.score = 0
        self.write(f"{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def win(self, winner):
        self.setposition(0, 0)
        self.write(f"{winner} Wins!", move=False, align=ALIGNMENT, font=FONT)
