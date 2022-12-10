# Make a border for the snake game
from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()

        # starting position
        self.penup()
        self.goto(-280, -280)

        self.pendown()
        self.goto(-280, 280)
        self.goto(280, 280)
        self.goto(280, -280)
        self.goto(-280, -280)
