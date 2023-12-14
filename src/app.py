"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db
from service import BDManagement

# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url.replace(
        "postgres://", "postgresql://"
    )
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# generate sitemap with all your endpoints
@app.route("/")
def sitemap():
    return generate_sitemap(app)


@app.route("/user", methods=["GET"])
def handle_hello():
    response_body = {"msg": "Hello, this is your GET /user response "}

    return jsonify(response_body), 200


@app.route("/item", methods=["GET"])
def get_item_list():
    item_list = BDManagement.get_item_list()
    return jsonify(item_list), 200


@app.route("/item/<int:item_id>", methods=["GET"])
def get_item_by_id(item_id):
    item_filtered = BDManagement.get_item_by_id(item_id)
    return jsonify(item_filtered), 200


@app.route("/item", methods=["POST"])
def add_item():
    request_body = request.json
    item_added = BDManagement.add_new_item(request_body)
    return jsonify(item_added), 200


@app.route("/character", methods=["GET"])
def get_character_list():
    character_list = BDManagement.get_character_list()
    return jsonify(character_list), 200


@app.route("/character/<int:character_id>", methods=["GET"])
def get_character_by_id(character_id):
    item_filtered = BDManagement.get_character_by_id(character_id)
    return jsonify(item_filtered), 200


@app.route("/planet", methods=["GET"])
def get_planet_list():
    planet_list = BDManagement.get_planet_list()
    return jsonify(planet_list), 200


@app.route("/planet/<int:planet_id>", methods=["GET"])
def get_planet_by_id(planet_id):
    planet_filtered = BDManagement.get_planet_by_id(planet_id)
    return jsonify(planet_filtered), 200


@app.route("/starship", methods=["GET"])
def get_starship_list():
    starship_list = BDManagement.get_starship_list()
    return jsonify(starship_list), 200


@app.route("/starship/<int:starship_id>", methods=["GET"])
def get_starship_by_id(starship_id):
    starship_filtered = BDManagement.get_starship_by_id(starship_id)
    return jsonify(starship_filtered), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=PORT, debug=False)
