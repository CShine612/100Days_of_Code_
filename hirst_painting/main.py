import colorgram, random
from turtle import Turtle, Screen


def extraction(image_name):
    colour_extract = colorgram.extract(image_name, 20)
    colour_list = []
    for i in colour_extract:
        r = i.rgb.r
        g = i.rgb.g
        b = i.rgb.b
        my_tup = (r, g, b)
        colour_list.append(my_tup)
    return colour_list


my_colours = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (224, 141, 211), (10, 97, 61)]

timmy = Turtle()
my_screen = Screen()
my_screen.colormode(255)
timmy.shape("turtle")

def hirst_grid(size):
    timmy.speed("fastest")
    my_screen.setworldcoordinates(-50, -50, size*50, size*50)
    for i in range(size):
        timmy.setposition(0, i * 50)
        for o in range(size):
            timmy.dot(30, random.choice(my_colours))
            timmy.penup()
            timmy.forward(50)
    timmy.hideturtle()
hirst_grid(5)

my_screen.exitonclick()
