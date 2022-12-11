from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.route("/")
def hello_world(name="World"):
    return f"hello {name}"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"


if __name__ == "__main__":
    app.run(debug=True)
