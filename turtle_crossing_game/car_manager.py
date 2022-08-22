from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1, 2)
        self.setposition(350, random.randint(-230, 250))
        self.setheading(180)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE + (self.level - 1) * MOVE_INCREMENT)


class CarManager:

    def __init__(self):
        self.level = 1
        self.cars = []

    def new_car(self):
        self.cars.append(Car(self.level))

    def level_up(self):
        self.level += 1
        for car in self.cars:
            car.level = self.level

    def move_cars(self):
        for car in self.cars:
            car.move()

    def purge_out_of_bounds(self):
        for car in self.cars:
            if car.xcor() > 350:
                del car

