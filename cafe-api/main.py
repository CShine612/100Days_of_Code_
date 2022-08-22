from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
import config

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def to_json(self):
        return jsonify(self.to_dict())


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return random_cafe.to_json()


@app.route("/all", methods=["GET"])
def all():
    cafes = db.session.query(Cafe).all()
    cafes_dict = {x: y.to_dict() for x, y in enumerate(cafes)}
    return jsonify(cafes_dict)


@app.route("/search", methods=["GET"])
def search():
    search_term = request.args.to_dict()["loc"]
    cafes = []
    for cafe in db.session.query(Cafe).all():
        if cafe.to_dict()["location"].lower() == search_term.lower():
            cafes.append(cafe)
    if len(cafes) > 0:
        return jsonify({x: y.to_dict() for x, y in enumerate(cafes)})
    else:
        return jsonify({"error": {"not found": "Sorry, we dont have a cafe at that location"}}), 404


@app.route("/add", methods=["POST"])
def add():
    data = request.form
    new_cafe = Cafe(name=data.get("name"),
                    map_url=data.get("map_url"),
                    img_url=data.get("img_url"),
                    location=data.get("location"),
                    seats=data.get("seats"),
                    has_toilet=bool(data.get("toilet")),
                    has_wifi=bool(data.get("wifi")),
                    has_sockets=bool(data.get("sockets")),
                    can_take_calls=bool(data.get("calls")),
                    coffee_price=data.get("coffee_price"))
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the cafe."}), 200


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    if db.session.query(Cafe).get(cafe_id):
        new_price = request.args.to_dict()["new_price"]
        cafe_to_update = db.session.query(Cafe).get(cafe_id)
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Successfully updated cafe entry"}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that ID was not found in the database"}), 404


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    if request.headers.get("api_key") == config.correct_key:
        if db.session.query(Cafe).get(cafe_id):
            cafe_to_delete = db.session.query(Cafe).get(cafe_id)
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"Success": "Successfully deleted cafe entry"}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, a cafe with that ID was not found in the database"}), 404
    else:
        return jsonify(error={"Unauthorised": "Sorry, you are not authorised to do that. Please confirm API key."})


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
