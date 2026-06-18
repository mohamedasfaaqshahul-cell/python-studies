from flask import Flask, render_template, request
from hostel import Hostel

app = Flask(__name__)

hostel = Hostel()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/allocate")
def allocate():

    regno = request.args.get("regno")
    name = request.args.get("name")
    gender = request.args.get("gender")
    year = int(request.args.get("year"))

    data = hostel.allocate_room(regno, name, gender, year)

    return render_template("result.html", data=data)

app.run(debug=True)
