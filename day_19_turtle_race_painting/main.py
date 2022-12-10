from turtle import Screen, Turtle


def move_fowards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_cw():
    tim.right(10)
    tim.forward(10)


def move_ccw():
    tim.left(10)
    tim.forward(10)


def clear():
    tim.clear()


def drawing():
    controls = [
        ("w", move_fowards),
        ("a", move_ccw),
        ("s", move_backwards),
        ("d", move_cw),
        ("c", clear),
    ]

    screen.listen()
    for control in controls:
        screen.onkey(
            key=control[0],
            fun=control[1],
        )


import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
NUM_OF_TURTLES = 6

# initialize turtles
for _ in range(NUM_OF_TURTLES):
    turtles.append(Turtle(shape="turtle"))

# move each turtle in position and change color
y = -300
color_index = 0
for turtle in turtles:
    turtle.penup()
    turtle.goto(x=-230, y=y)
    turtle.color(colors[color_index])
    y += 100
    color_index += 1

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
