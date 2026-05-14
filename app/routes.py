from app import create_app
from flask import Blueprint, render_template, jsonify
from app.data import load_all_data
from app.db import get_graph_data

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

bp = blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/api/load")
def load_data():
    load_all_data()
    return jsonify({"status": "done"})

@bp.route("api/graph")
def grpah():
    data = get_graph_data()
    return jsonify(data)