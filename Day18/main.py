from turtle import Turtle, Screen
from random import random, choice

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
sides = 4

def random_heading():
    headings = [0, 45, 90, 135, 180, 225, 270, 315]
    heading = choice(headings)
    timmy.setheading(heading)

def random_colour():
    r = random()
    g = random()
    b = random()

    timmy.color(r, g, b)

def polygon(sides):
    for i in range(sides):
        timmy.forward(100)
        timmy.right(360/sides)

def dashed_line(length, dash_len=10):
    total = 0
    pen = 0
    while total < length:
        if pen == 0:
            timmy.forward(dash_len)
            timmy.penup()
            pen = 1
        elif pen == 1:
            timmy.forward(dash_len)
            timmy.pendown()
            pen = 0
        total += dash_len

def multi_polys(polys):
    for i in range(polys+1):
        if i > 2:
            random_colour()
            polygon(i)

def random_walk(steps):
    timmy.speed(10)
    timmy.pensize(10)
    for i in range(steps):
        random_colour()
        random_heading()
        timmy.forward(30)
    timmy.pensize(1)
    timmy.speed(6)

def spirograph(num):
    timmy.speed("fastest")
    for i in range(num):
        random_colour()
        timmy.circle(100)
        timmy.left(360/num)
    timmy.speed(6)


spirograph(100)

screen = Screen()

screen.exitonclick()