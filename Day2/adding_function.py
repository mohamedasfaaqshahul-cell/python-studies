ADDING:
passengers = ["assu"]
passengers.append("sarah")
passengers.insert(0, "sahana")
print(passengers)

FUNCTION WITH LIST:
def show_passengers(passenger_list):
    print("Total Passengers:", len(passenger_list))

    for passenger in passenger_list:
        print("-", passenger)

my_passengers = ["Assu", "Mohamed", "Sahana"]

show_passengers(my_passengers)
