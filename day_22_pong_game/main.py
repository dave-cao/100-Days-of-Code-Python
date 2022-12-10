import time
from turtle import Screen, Turtle

from ball import Ball
from border import Border
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


border = Border(width=800, height=600)
paddle_one = Paddle(350, 0)
paddle_two = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle_one.go_up, "Up")
screen.onkey(paddle_one.go_down, "Down")
screen.onkey(paddle_two.go_up, "w")
screen.onkey(paddle_two.go_down, "s")


game_over = False
while not game_over:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.reverse_y_direction()

    # detect collision with right paddle and left paddle
    if (
        ball.distance(paddle_one) < 50
        and ball.xcor() > 320
        or ball.distance(paddle_two) < 50
        and ball.xcor < -320
    ):
        ball.reverse_x_direction()

    # detect collision with right wall
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # detect collision with left wall
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
