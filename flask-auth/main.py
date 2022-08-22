from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if db.session.query(User).filter(User.email == request.form.get("email")).first():
            flash("User with that email already exists. Please login.")
            return redirect(url_for("login", logged_in=current_user.is_authenticated))
        new_user = User(email=request.form.get("email"),
                        password=generate_password_hash(password=request.form.get("password"),
                                                                          method='pbkdf2:sha256',
                                                                          salt_length=8),
                        name=request.form.get("name")
                        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets", user=new_user, logged_in=current_user.is_authenticated))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        if db.session.query(User).filter(User.email == email).first():
            user = db.session.query(User).filter(User.email == email).first()
            if check_password_hash(user.password, request.form.get("password")):
                login_user(user)
                return redirect(url_for("secrets", user=user, logged_in=current_user.is_authenticated))
            else:
                flash('Incorrect Password')
                return redirect(url_for("login", logged_in=current_user.is_authenticated))
        else:
            flash('That email is not registered')
            return redirect(url_for("login", logged_in=current_user.is_authenticated))
    else:
        return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    user = current_user
    return render_template("secrets.html", user=user, logged_in=current_user.is_authenticated)


@app.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login", logged_in=current_user.is_authenticated))


@app.route('/download')
@login_required
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
