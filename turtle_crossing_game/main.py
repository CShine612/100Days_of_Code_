import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

car_manager = CarManager()

game_is_on = True
while game_is_on:
    car_manager.purge_out_of_bounds()
    if random.randint(0, 1):
        if random.randint(0, car_manager.level):
            for _ in range(random.randint(0, 2)):
                car_manager.new_car()
    car_manager.move_cars()
    time.sleep(0.1)
    if player.is_at_finish():
        player.level_up()
        car_manager.level_up()
        scoreboard.level_up()
    for car in car_manager.cars:
        if car.distance(player) < 30 and car.ycor() + 15 > player.ycor() > car.ycor() - 15:
            scoreboard.game_over()
            game_is_on = False
    screen.update()



screen.exitonclick()