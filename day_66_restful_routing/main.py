from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
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
        """Return object data in easily serializable format"""
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


with app.app_context():
    cafes = db.session.query(Cafe).all()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/random", methods=["GET"])
def random():
    random_cafe = Cafe.query.order_by(func.random()).first().to_dict()
    return jsonify(cafe=random_cafe)


@app.route("/all", methods=["GET"])
def all():

    return jsonify([cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search():
    loc = request.args.get("loc")
    intended_cafe = [cafe for cafe in cafes if cafe.location == loc]
    if intended_cafe:
        return jsonify(cafe=intended_cafe[0].to_dict())
    else:
        return jsonify(
            error={"Not Found": "Sorry, we don't have a cafe at that location."}
        )


## HTTP GET - Read Record

## HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        id=request.form.get("id"),
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )

    with app.app_context():
        db.session.add(new_cafe)
        db.session.commit()

    return jsonify({"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["GET", "PATCH"])
def update(cafe_id):
    new_price = request.args.get("new_price")
    with app.app_context():
        cafe_to_update = db.session.query(Cafe).get(cafe_id)

        if cafe_to_update:
            cafe_to_update.coffee_price = new_price
            db.session.commit()

            return jsonify(response={"success": "Successfully updated record"})

    return jsonify(response={"error": "Could not find cafe"}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):

    api_key = request.args.get("api-key")
    with app.app_context():
        cafe = db.session.query(Cafe).get(cafe_id)

        if cafe and api_key == "TopSecretAPIKey":
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "The record has been deleted"})

    return (
        jsonify(
            response={
                "error": "Something went wrong, did you provide the correct API key?"
            }
        ),
        403,
    )


if __name__ == "__main__":
    app.run(debug=True)
