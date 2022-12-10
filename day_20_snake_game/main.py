import time
from turtle import Screen, Turtle

from border import Border
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create items
snake = Snake()
food = Food()
scoreboard = Scoreboard()
border = Border()

# Move snake on button press
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # make sure the all the body of the snake gets updates at one time
    screen.update()
    time.sleep(0.05)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    tail = snake.squares[1:]
    for segment in tail:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
