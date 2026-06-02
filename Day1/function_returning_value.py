def create_email_id(name):
    email_id = name.lower() + "@gmail.com"
    return email_id

name = input("Enter your name: ")

email = create_email_id(name)
print(email)
