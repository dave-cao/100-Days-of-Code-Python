# Make a border for the pong game
from turtle import Turtle


class Border(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.color("white")
        self.hideturtle()

        x_cor = width / 2
        y_cor = height / 2

        # starting position
        self.penup()
        self.goto(-x_cor, -y_cor)

        self.pendown()
        self.goto(-x_cor, y_cor)
        self.goto(x_cor, y_cor)
        self.goto(x_cor, -y_cor)
        self.goto(-x_cor, -y_cor)
