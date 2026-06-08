def book_seat(flight_id, details):
    print("\nFlight Found")
    print("Flight Number :", flight_id)
    print("Source :", details["source"])
    print("Destination :", details["dest"])
    print("Available Seats :", details["seats"])
    print("Ticket Price :", details["price"])

    seats_required = int(input("\nHow many seats do you want to book? "))

    if seats_required <= details["seats"]:
        details["seats"] = details["seats"] - seats_required

        print("\nBooking Confirmed")
        print("Seats Booked :", seats_required)
        print("Remaining Seats :", details["seats"])
    else:
        print("\nBooking Failed")
        print("Not enough seats available")
