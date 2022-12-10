# Create a scoreboard for the snake game
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 230)

        self.score = 0
        self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} Highscore: {self.high_score}",
            False,
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
