from Flight_Dictionary import flights
from Search_Flight import search_flight
from Book_Flight import book_seat

source = input("Enter Source: ")
destination = input("Enter Destination: ")

flight_id, details = search_flight(source, destination, flights)

if flight_id:
    print(details)

    seats = int(input("Enter seats: "))

    if book_seat(details, seats):
        print("Booking Confirmed")
        print("Remaining Seats:", details["seats"])
    else:
        print("Seats not available")
else:
    print("Flight not found")
