# Create the bouncing ball for pong

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

        self.new_x = self.xcor()
        self.new_y = self.ycor()

        self.x_speed = 10
        self.y_speed = 10

    def move(self):
        self.new_x += self.x_speed
        self.new_y += self.y_speed
        self.goto(self.new_x, self.new_y)

    def reverse_y_direction(self):
        self.y_speed *= -1

    def reverse_x_direction(self):
        self.x_speed *= -1

    def reset_ball(self):
        self.new_x = 0
        self.new_y = 0
        self.reverse_x_direction()
