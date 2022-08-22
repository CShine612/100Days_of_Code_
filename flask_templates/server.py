import datetime
import random
import requests

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    year = datetime.datetime.now().year
    random_number = random.randint(0, 100)
    return render_template("index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def name_guesser(name):
    gender = requests.get(f"https://api.genderize.io?name={name.lower()}").json()["gender"]
    age = requests.get(f"https://api.agify.io?name={name.lower()}").json()["age"]
    return render_template("guess.html", name=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run()

