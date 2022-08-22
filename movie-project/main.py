from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

import config

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
db = SQLAlchemy(app)


class EditForm(FlaskForm):
    rating = StringField("Please enter your new rating.", validators=[DataRequired()])
    review = StringField("Please enter your new review.", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddForm(FlaskForm):
    title = StringField("Please type the name of the movie you would like to add.", validators=[DataRequired()])
    submit = SubmitField("Submit")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.String(4))
    description = db.Column(db.String(280))
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250))

    def __repl__(self):
        return '<Movie %r>' % self.title


#db.create_all()
#
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    top_ten = []
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    for i in range(10, 0, -1):
        if Movie.query.filter_by(ranking=i).first():
            top_ten.append(Movie.query.filter_by(ranking=i).first())
    return render_template("index.html", top_ten=top_ten)


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    form = EditForm()
    if form.validate_on_submit():
        movie_to_update = Movie.query.get(id)
        movie_to_update.rating = form.rating.data
        movie_to_update.review = form.review.data
        db.session.commit()
        return home()
    return render_template("edit.html", form=form)


@app.route("/delete/<id>")
def delete(id):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return home()


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        parameters = {"api_key": config.tmbd_api_key,
                      "query": form.title.data}
        response = requests.get(config.tmdb_endpoint, params=parameters)
        response.raise_for_status()

        data = response.json()["results"]

        return render_template("select.html", results=data)
    return render_template("add.html", form=form)


@app.route("/add_selected/<movie_id>")
def add_selected(movie_id):
    parameters = {"api_key": config.tmbd_api_key}
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params=parameters)
    response.raise_for_status()
    movie_data = response.json()

    new_movie = Movie(title=movie_data["title"],
                      year=movie_data["release_date"][:4],
                      description=movie_data["overview"],
                      rating=movie_data["vote_average"],
                      img_url=f"{config.tmdb_image_root}{movie_data['poster_path']}")

    db.session.add(new_movie)

    db.session.commit()
    movie_internal_id = Movie.query.filter_by(title=movie_data["title"]).first().id
    print(movie_internal_id)
    return redirect(url_for("edit", id=movie_internal_id))

if __name__ == '__main__':
    app.run(debug=True)
