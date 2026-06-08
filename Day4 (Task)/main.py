from Search_Flight import search_flight
from Book_Seat import book_seat

def main():
    source = input("Enter Source Airport: ")
    destination = input("Enter Destination Airport: ")

    flight_id, details = search_flight(source, destination)

    if flight_id:
        book_seat(flight_id, details)
    else:
        print("No flights available for this route")

main()
