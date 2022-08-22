from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        for pos in STARTING_POS:
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.setposition(pos[0], 0)
            self.segments.append(new_seg)
        self.head = self.segments[0]
        self.head.setheading(0)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        xcor = self.segments[-1].xcor()
        ycor = self.segments[-1].ycor()
        new_seg.setposition(xcor, ycor)
        self.segments.append(new_seg)

    def reset(self):
        for segment in self.segments:
            segment.setposition(1000, 1000)
        self.segments.clear()
        self.__init__()

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
