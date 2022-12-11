import random

from flask import Flask

app = Flask(__name__)


random_number = random.randint(0, 9)
print(f"The random number is {random_number}")


@app.route("/")
def main():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:number>")
def guess_number(number):
    if number < random_number:
        return "<h1 style='color:red'>Too low! Try again!</h1><img src='https://media.giphy.com/media/gfsQffBnuc6e096brx/giphy.gif'>"
    elif number > random_number:
        return "<h1 style='color:purple'>Too high! Try Again!</h1><img src='https://media.giphy.com/media/AUYhIMdGrg23e/giphy.gif'>"
    else:
        return "<h1 style='color:green'>You found me!</h1><img src='https://media.giphy.com/media/TdfyKrN7HGTIY/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
