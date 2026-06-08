def book_seat(details, seats):
    if seats <= details["seats"]:
        details["seats"] -= seats
        return True
    return False
