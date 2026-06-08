def search_flight(source, destination, flights):
    for flight_id, details in flights.items():
        if details["source"].lower() == source.lower() and details["dest"].lower() == destination.lower():
            return flight_id, details

    return None, None
