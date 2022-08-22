from turtle import Turtle
import random

SPEED = 20
SHAPE = "circle"
COLOUR = "white"


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOUR)
        self.shape(SHAPE)
        self.penup()

    def serve(self):
        self.setposition(0, 0)
        self.setheading(random.randint(135, 225) + random.choice((0, 180)))
        self.settiltangle(0)

    def move(self):
        self.forward(SPEED)

    def wall_bounce(self):
        if self.ycor() > 390 or self.ycor() < -390:
            new_heading = self.heading() - 2 * (self.heading() - 180)
            self.setheading(new_heading)
        self.settiltangle(0)

    def pong_bounce(self):
        new_heading = self.heading() - 2 * (self.heading() - 90)
        self.setheading(new_heading)
        self.settiltangle(0)
