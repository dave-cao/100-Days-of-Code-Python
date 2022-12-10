# The Hirst Painting Project
# Colorgram
# import colorgram

# colors = colorgram.extract("image.jpg", 30)
# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_list.append((r, g, b))
#
# print(rgb_list)
import random

rgb_list = [
    (54, 108, 149),
    (225, 201, 108),
    (134, 85, 58),
    (224, 141, 62),
    (197, 144, 171),
    (143, 180, 206),
    (137, 82, 106),
    (210, 90, 68),
    (232, 226, 194),
    (188, 78, 122),
    (69, 101, 86),
    (132, 183, 132),
    (65, 156, 86),
    (137, 132, 74),
    (48, 155, 195),
    (183, 191, 202),
    (232, 221, 225),
    (58, 47, 41),
    (47, 59, 96),
    (38, 44, 64),
    (106, 46, 54),
    (41, 55, 48),
    (12, 104, 95),
    (118, 125, 145),
    (182, 194, 199),
    (215, 176, 187),
    (223, 178, 168),
    (54, 45, 52),
]

# 10 by 10 dots
from turtle import Screen, Turtle

dot = Turtle()
dot.penup()
start_x = -400
start_y = -200
dot.goto(start_x, start_y)
screen = Screen()
screen.colormode(255)

for _ in range(10):
    dot.goto(start_x, start_y)
    for _ in range(10):
        dot_color = random.choice(rgb_list)
        dot.dot(20, dot_color)
        dot.forward(80)
    start_y += 50


screen.exitonclick()
