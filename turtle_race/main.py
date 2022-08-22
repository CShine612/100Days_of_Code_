from turtle import Turtle, Screen
import random

colours = {"r": "red", "o": "orange", "y": "yellow", "g": "green", "b": "blue", "p": "purple"}
my_screen = Screen()
racers = []
my_screen.setworldcoordinates(-50, -50, 1050, len(colours)*50)

finish = Turtle()
finish.hideturtle()
finish.penup()
finish.setposition(1000,-100)
finish.pensize(5)
finish.pendown()
finish.setposition(1000, len(colours)*50)


for ind, colour in enumerate(list(colours.values())):
    exec(colour + "= Turtle()")
    exec(colour + ".penup()")
    exec(f"{colour}.color('{colour}')")
    exec(colour + ".shape('turtle')")
    start_position = (0, 50*ind)
    exec(f"{colour}.setposition({start_position[0]}, {start_position[1]})")
    exec(f"racers.append({colour})")

def turn():
    for racer in racers:
        racer.forward(random.randint(1,50))

def check_win():
    winner = False
    for racer in racers:
        if racer.xcor() > 1000:
            if winner and racer.xcor > winner.xcor():
                winner = racer
            else:
                winner = racer

    return winner

def race():
    player = ""
    while player.lower() not in list(colours.keys()):
        player = input("Please choose a colour: r,o,y,g,b,p: ")
    player_colour = colours[player]
    while not check_win():
        turn()
    if player_colour == check_win():
        print("congratulations")
    else:
        print("You're just a loser")

race()


my_screen.exitonclick()