def validate_registration(name, gmail_id, phone_number):
    if name == "" or gmail_id == "" or phone_number == "":
        print("Error: All fields are required!")
        return False

    print("Gmail registration form is valid.")
    return True

name = input("Enter Name: ")
gmail_id = input("Enter Gmail ID: ")
phone_number = input("Enter Phone Number: ")

validate_registration(name, gmail_id, phone_number)
