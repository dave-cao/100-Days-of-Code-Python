# Day 18 is using the Turtle and GUI to create a turtle project
# -- Intermediate --
import random
from turtle import Screen, Turtle

turtle = Turtle()


def challenge_4():
    """Create a turtle that draws a triangle, square...up to decagon
    with different colours for each shape"""
    colors = ["red", "orange", "yellow", "purple", "blue", "pink", "green", "violet"]
    for size in range(3, 11):
        angle = 360 / size
        turtle.pencolor(colors[size - 3])
        print(angle)
        for _ in range(size):
            turtle.forward(100)
            turtle.right(angle)


def switch(x, y):
    screen.exitonclick()
    print(x, y)


# Random walk
def challenge_2():
    """Create a random walk program with turtle"""
    screen.colormode(255)
    turtle.width(10)
    turtle.hideturtle()
    turtle.speed(0)
    while True:
        turtle.forward(20)
        turtle.pencolor(
            (
                (random.randint(1, 255)),
                (random.randint(1, 255)),
                (random.randint(1, 255)),
            )
        )
        if not random.randint(0, 1):
            turtle.left(90)
        else:
            turtle.right(90)
        screen.onclick(switch)


def random_color():
    """rgb is a tuple of integers"""
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return (r, g, b)


def challenge_5():
    # Make a spirograph
    turtle.shape("turtle")
    turtle.hideturtle()
    turtle.speed(0)
    screen = Screen()
    screen.colormode(255)

    for _ in range(360):

        turtle.color(random_color())
        turtle.circle(200)
        turtle.right(10)


screen.exitonclick()
