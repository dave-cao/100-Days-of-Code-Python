# The snake class for my snake game
from turtle import Turtle


class Snake:
    def __init__(self):
        self.squares = []
        self.STARTING_SIZE = 3
        self.UP = 90
        self.LEFT = 180
        self.DOWN = 270
        self.RIGHT = 360

        self.initialize_snake()
        self.place_snake()

        self.head = self.squares[0]

    def initialize_snake(self):
        """Put starting squares into list"""
        for _ in range(self.STARTING_SIZE):
            self.squares.append(Turtle(shape="square"))

    def place_snake(self):
        """Place starting position for snake"""
        x = 0
        y = 0
        for square in self.squares:
            square.color("white")
            square.penup()
            square.goto(x, y)
            x -= 20

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.initialize_snake()
        self.place_snake()
        self.head = self.squares[0]

    def add_segment(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def extend(self):
        """Add segment to end of snake"""
        self.add_segment(self.squares[-1].position())

    def move(self):
        """Move the snake by copying the square in front of it.
        This allows left and right movement"""

        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        """Moves snake up"""
        x_movement = self.head.xcor() - self.squares[1].xcor()
        # if the snake is moving right
        if x_movement > 0:
            self.head.left(90)

        # if the snake is moving left
        if x_movement < 0:
            self.head.right(90)

    def down(self):
        """Moves snake down"""
        x_movement = self.head.xcor() - self.squares[1].xcor()
        # if the snake is moving right
        if x_movement > 0:
            self.head.right(90)

        # if the snake is moving left
        if x_movement < 0:
            self.head.left(90)

    def left(self):
        """Moves snake left"""
        y_movement = self.head.ycor() - self.squares[1].ycor()
        # if the snake is moving up
        if y_movement > 0:
            self.head.left(90)

        # if the snake is moving down
        if y_movement < 0:
            self.head.right(90)

    def right(self):
        """Moves snake right"""
        y_movement = self.head.ycor() - self.squares[1].ycor()
        # if the snake is moving up
        if y_movement > 0:
            self.head.right(90)

        # if the snake is moving down
        if y_movement < 0:
            self.head.left(90)
