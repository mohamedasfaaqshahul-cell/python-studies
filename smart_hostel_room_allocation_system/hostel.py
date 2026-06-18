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

        return {
            "regno": regno,
            "name": name,
            "gender": gender,
            "year": year,
            "block": block,
            "room": room
        }
