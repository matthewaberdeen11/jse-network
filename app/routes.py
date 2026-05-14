from flask import Blueprint, render_template, jsonify
from app.data import load_all_data
from app.db import get_graph_data
from app.db import get_graph_data, get_directors

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/api/load")
def load_data():
    load_all_data()
    return jsonify({"status": "done"})

@bp.route("/api/graph")
def grpah():
    data = get_graph_data()
    return jsonify(data)

@bp.route("/api/directors/<symbol>")
def directors(symbol):
    data = get_directors(symbol)
    return jsonify(data)