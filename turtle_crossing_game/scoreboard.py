from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
POSITION = (-210, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(POSITION)

        self.level = 1
        self.write(f"Level = {self.level}", move = False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level = {self.level}", move = False, align=ALIGNMENT, font=FONT)
