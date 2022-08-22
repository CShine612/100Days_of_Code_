from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_emphisis(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/bye")
@make_bold
@make_emphisis
@make_underline
def bye():
    return "Bye"


if __name__ == "__main__":
    app.run()
