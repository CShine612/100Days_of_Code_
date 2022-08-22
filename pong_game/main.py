from turtle import Screen, Turtle
from pong import Pong
from ball import Ball
from scoreboard import Scoreboard
import time

GAME_SPEED = 0.1
CPU_PADDLE_LENGTH = 160


sleep = GAME_SPEED
# Set up game screen
screen = Screen()
screen.setup(1600, 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Set up center line drawing turtle
center_line = Turtle()
center_line.hideturtle()
center_line.color("white")
center_line.pensize(10)
center_line.penup()
center_line.setposition(0, -405)
center_line.setheading(90)

# Loop to draw center line
for i in range(20):
    center_line.forward(20)
    center_line.pendown()
    center_line.forward(20)
    center_line.penup()

# Set up scoreboard
player_score = Scoreboard((-100, 300))
cpu_score = Scoreboard((100, 300))

# Set up Player paddle
player_pong = Pong()
player_pong.setposition(-710, 0)

# Set up CPU paddle
cpu_pong = Pong()
cpu_pong.setposition(710, 0)
cpu_pong.size_change(CPU_PADDLE_LENGTH)

# Set up ball
ball = Ball()
ball.serve()

# Set up screen listening and related functions
screen.listen()
screen.onkey(player_pong.up, "Up")
screen.onkey(player_pong.down, "Down")

# Game control parameter
game_is_on = True


# Group of actions performed when the ball passes the paddle
def paddle_miss():
    ball.move()
    time.sleep(sleep)
    cpu_score.add_point()
    screen.update()
    ball.serve()


# Main game loop
while game_is_on:
    if ball.xcor() < -685:
        if player_pong.ycor() + player_pong.length/2 > ball.ycor() > player_pong.ycor() - player_pong.length/2:
            ball.pong_bounce()
            sleep = sleep * 0.9
        else:
            paddle_miss()
            sleep = GAME_SPEED
    elif ball.xcor() > 685:
        if cpu_pong.ycor() + cpu_pong.length/2 > ball.ycor() > cpu_pong.ycor() - cpu_pong.length/2:
            ball.pong_bounce()
            sleep = sleep * 0.9
        else:
            paddle_miss()
            sleep = GAME_SPEED
    ball.wall_bounce()
    ball.move()
    cpu_pong.cpu_move()
    screen.update()
    time.sleep(sleep)

    if cpu_score.score > 10:
        game_is_on = False
        cpu_score.win("Computer")
    elif player_score.score > 10:
        game_is_on = False
        cpu_score.win("Player")
screen.update()

screen.exitonclick()
