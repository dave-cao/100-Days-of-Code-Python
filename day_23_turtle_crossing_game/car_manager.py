import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 0.5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = 0.5

    def generate_cars(self, x):
        car = Turtle(shape="square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(x, random.randint(-300, 300))
        car.color(random.choice(COLORS))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def change_speed(self):
        self.car_speed += 1
