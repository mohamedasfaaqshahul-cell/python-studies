from flask import Flask, request

app = Flask(__name__)

class Hostel:

    def allocate_room(self, regno, name, gender, year):

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

        return f"""
        <h1>Smart Hostel Room Allocation System</h1>

        <h3>Student Details</h3>

        Register Number : {regno}<br>
        Name : {name}<br>
        Gender : {gender}<br>
        Year : {year}<br><br>

        <h3>Room Allocation Details</h3>

        Hostel Block : {block}<br>
        Room Number : {room}<br>
        """

hostel = Hostel()

@app.route("/")
def home():

    return """
    <h1>Smart Hostel Room Allocation System</h1>

    <form action="/allocate">

        Register Number:
        <input type="text" name="regno"><br><br>

        Student Name:
        <input type="text" name="name"><br><br>

        Gender:
        <input type="text" name="gender"><br><br>

        Year:
        <input type="number" name="year"><br><br>

        <input type="submit" value="Allocate Room">

    </form>
    """

@app.route("/allocate")
def allocate():

    regno = request.args.get("regno")
    name = request.args.get("name")
    gender = request.args.get("gender")
    year = int(request.args.get("year"))

    return hostel.allocate_room(
        regno,
        name,
        gender,
        year
    )

app.run(debug=True)
