Ex3:
pending_bookings = []
pending_bookings.append("Assu")
pending_bookings.append("Mohamed")
pending_bookings.append("Sahana")
print("Total Bookings:", len(pending_bookings))
pending_bookings.pop(1)
print(pending_bookings)

Ex4:
passengers = [
    {"city":"Coimbatore","name":"Assu"},
    {"city":"Madurai","name":"Mohamed"},
    {"city":"Chennai","name":"Sahana"}
]

for passenger in passengers:
    if passenger["city"] == "Coimbatore":
        print(passenger["name"])
