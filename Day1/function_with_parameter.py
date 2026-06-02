def show_user(name, email, phone):
    print("---- Gmail User Details ----")
    print(f"Name  : {name}")
    print(f"Email : {email}")
    print(f"Phone : {phone}")

name = input("Enter Name: ")
email = input("Enter Gmail ID: ")
phone = input("Enter Phone Number: ")

show_user(name, email, phone)
