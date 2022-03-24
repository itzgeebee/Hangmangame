from pprint import pprint

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

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
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def random():
    all_cafes = Cafe.query.all()
    random_cafe = choice(all_cafes)
    # cafe = jsonify(cafe=jsonify(id=random_cafe.id,
    #                             name=random_cafe.name,
    #                             map_url=random_cafe.map_url,
    #                             img_url=random_cafe.img_url,
    #                             location=random_cafe.location,
    #                             has_socket=random_cafe.has_sockets,
    #                             has_toilet=random_cafe.has_toilet,
    #                             has_wifi=random_cafe.has_wifi,
    #                             can_take_calls=random_cafe.can_take_calls,
    #                             seats=random_cafe.seats,
    #                             coffee_price=random_cafe.coffee_price).json
    #                ).json
    cafe_json = jsonify(cafe=random_cafe.to_dict()).json

    return cafe_json


@app.route("/all", methods=["GET"])
def all():
    all_cafes = Cafe.query.all()
    caf_list = []
    for i in all_cafes:
        caf = i.to_dict()
        caf_list.append(caf)

    all_cafes_json = jsonify(cafes=caf_list).json
    pprint(all_cafes_json)

    return all_cafes_json


@app.route("/search", methods=["GET"])
def search():
    loc = request.args.get("location")
    all_cafe = Cafe.query.filter_by(location=loc).all()
    if not all_cafe:
        return jsonify({"error": {"Not found": "Sorry we do not have a cafe at that location"}})
    else:
        cafes = []
        for i in all_cafe:
            result = {"cafe": i.to_dict()}
            cafes.append(result)

        all_cafes_json = jsonify(cafes=cafes).json
        pprint(all_cafes_json)
        return all_cafes_json


@app.route("/add", methods=["POST"])
def add():
    loc = request.args.get("location")
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url= request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({"response":{"success":"Successfully added the new cafe"}})


@app.route("/update-price/<int:cafe_id>", methods=["GET", "PATCH"])
def update_price(cafe_id):
    cafe_wanted = Cafe.query.get(cafe_id)
    if cafe_wanted:
        price = request.args.get("price")
        cafe_wanted.coffee_price = price
        db.session.commit()
        return jsonify({"success":"Successfully updated the price"})
    else:
        return jsonify({"error":{
            "Not found": "Sorry, a cafe with that id was not found in the database"
        }}), 404

        
@app.route("/delete/<int:cafe_id>", methods=["GET", "DELETE"])
def report_closed(cafe_id):
    cafe_wanted = Cafe.query.get(cafe_id)
    api_key = "top-secret-key"
    key = request.args.get("key")
    if key == api_key:
        if cafe_wanted:
            db.session.delete(cafe_wanted)
            db.session.commit()
            return jsonify({"success":"Successfully deleted"})
        else:
            return jsonify({"error":{
                "Not found": "Sorry, a cafe with that id was not found in the database"
            }}), 404

    elif not key or key!=api_key:
        return jsonify({"Forbidden": {
            "Key error":"please enter a valid API key"
        }}), 403




if __name__ == '__main__':
    app.run(debug=True)
