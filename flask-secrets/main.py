from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
import config

csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)
Bootstrap(app)
app.secret_key = config.random_string


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == config.correct_login and form.password.data == config.correct_pass:
            return success()
        else:
            return denied()
    return render_template("login.html", form=form)

def success():
    return render_template("success.html")

def denied():
    return render_template("denied.html")


if __name__ == '__main__':
    app.run(debug=True)
