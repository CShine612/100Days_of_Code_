from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()
my_screen.listen()

def forwards():
    timmy.forward(10)
def backwards():
    timmy.back(10)
def left():
    timmy.left(10)
def right():
    timmy.right(10)
def clear():
    timmy.home()
    timmy.clear()

my_screen.onkey(key="w", fun=forwards)
my_screen.onkey(key="s", fun=backwards)
my_screen.onkey(key="a", fun=left)
my_screen.onkey(key="d", fun=right)
my_screen.onkey(key="c", fun=clear)

my_screen.exitonclick()
