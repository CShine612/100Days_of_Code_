from turtle import Turtle

PADDLE_LENGTH = 120


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.length = PADDLE_LENGTH
        self.order = 1
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(1.5, self.length/20)
        self.setheading(90)

    def up(self):
        if self.ycor() < 340:
            self.forward(20)

    def down(self):
        if self.ycor() > -340:
            self.backward(20)

    def cpu_move(self):
        if self.ycor() > 380 - self.length/2:
            self.order = 0
        elif self.ycor() < -380 + self.length/2:
            self.order = 1
        if self.order == 1:
            self.up()
        else:
            self.down()

    def size_change(self, length):
        self.length = length
        self.shapesize(1.5, self.length / 20)
