from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setposition(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.setposition(0, -280)

    def is_at_finish(self):
        return self.ycor() > FINISH_LINE_Y
