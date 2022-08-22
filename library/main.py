from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)

all_books = []


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.Column(db.Float)

    def __repr__(self):
        return '<Book %r>' % self.title


# db.create_all()


class add_book_form(FlaskForm):
    name = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Author Name", validators=[DataRequired()])
    rating = SelectField("Rating", validators=[DataRequired()], choices=[num for num in range(11)])
    submit = SubmitField("Submit")

class edit_book_form(FlaskForm):
    rating = SelectField("Rating", validators=[DataRequired()], choices=[num for num in range(11)])
    submit = SubmitField("Change Rating")


@app.route('/')
def home():
    global all_books
    if len(Book.query.all()) > 0:
        all_books = [{"id": book.id,
                  "title": book.title,
                  "author": book.author,
                  "rating": book.rating}
                 for book in Book.query.all()]
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = add_book_form()
    if form.validate_on_submit():
        book = Book(title=form.name.data,
                    author=form.author.data,
                    rating=form.rating.data)
        db.session.add(book)
        db.session.commit()
        return home()

    return render_template("add.html", form=form)


@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit(book_id):
    form = edit_book_form()
    book_to_update = Book.query.get(book_id)
    if form.validate_on_submit():
        book_to_update.rating = form.rating.data
        db.session.commit()
        return home()
    return render_template("edit.html", title=book_to_update.title, rating=book_to_update.rating, form=form)

@app.route("/delete/<book_id>")
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return home()

if __name__ == "__main__":
    app.run(debug=True)
