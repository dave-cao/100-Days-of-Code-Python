import random
import time
from turtle import Screen

from border import Border
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

border = Border(600, 600)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
second = 0
car_generation_speed = 100
while game_is_on:
    time.sleep(0.01)
    screen.update()
    second += 1

    # Restart position of player once they past the finish line
    if player.crossed_level():
        player.start()
        scoreboard.increase_score()
        car_manager.change_speed()
        car_generation_speed /= 4

    # randomly populate cars in beginning of game
    if second < 20:
        car_manager.generate_cars(random.randint(-300, 300))

    # populate cars from left to right at a certain speed
    if not second % car_generation_speed:
        car_manager.generate_cars(320)
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 30 and scoreboard.score != 0:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
