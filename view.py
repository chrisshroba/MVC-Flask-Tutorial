__author__ = 'cshroba'

import control

from flask import *

app = Flask(__name__, static_folder="static", static_path="")

@app.route("/note/<id>")
def get_note(id):
    return control.get_note(id)


@app.route("/create", methods=["POST"])
def create_note():
    print 1
    id = request.form["id"]
    print 2
    note = request.form["note"]
    print 3
    return control.save_note(id, note)


app.run(debug=True)