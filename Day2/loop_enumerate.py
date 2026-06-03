FOR LOOP:
passengers = ["ASSU", "MOHAMED", "SAHANA"]
for passenger in passengers:
    print("Passenger:", passenger)

ENUMERATE:
passengers = ["ASSU", "MOHAMED", "SAHANA"]
for index, passenger in enumerate(passengers, start=1):
    print(f"{index}. {passenger}")

WHILE LOOP:
count = 0
max_bookings = 3
while count < max_bookings:
    print(f"Booking Flight Ticket #{count+1}")
    count += 1
print("Booking Closed")
