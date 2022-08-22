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
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score = {self.score} High Score = {self.high_score}", move = False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score} High Score = {self.high_score}", move = False, align=ALIGNMENT, font=FONT)


