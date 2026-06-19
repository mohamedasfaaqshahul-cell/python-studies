from flask import Flask, render_template, request

app = Flask(__name__)

# Step 1 - Show search form
@app.route("/")
def home():
    return render_template("search.html")


# Step 2 - Allocate room
@app.route("/search", methods=["POST"])
def search():

    regno = request.form["regno"]
    name = request.form["name"]
    gender = request.form["gender"]
    year = int(request.form["year"])

    if gender.lower() == "male":
        block = "Boys Hostel"
    else:
        block = "Girls Hostel"

    if year == 1:
        room = "A101"
    elif year == 2:
        room = "B201"
    elif year == 3:
        room = "C301"
    else:
        room = "D401"

    return render_template(
        "room.html",
        regno=regno,
        name=name,
        gender=gender,
        year=year,
        block=block,
        room=room
    )


# Step 3 - Confirm allocation
@app.route("/book", methods=["POST"])
def book():

    regno = request.form["regno"]
    name = request.form["name"]
    gender = request.form["gender"]
    year = request.form["year"]
    block = request.form["block"]
    room = request.form["room"]

    return render_template(
        "success.html",
        regno=regno,
        name=name,
        gender=gender,
        year=year,
        block=block,
        room=room
    )


if __name__ == "__main__":
    app.run(debug=True)
