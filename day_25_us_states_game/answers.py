from turtle import Turtle


class Answer(Turtle):
    def __init__(self, x, y, state):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto((x, y))
        self.write(state.title(), align="center", font=("Courier", 10, "normal"))
