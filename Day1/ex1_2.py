# EXERCISE 1 :

name = input("Enter your name: ")
gmail_id = input("Enter your Gmail ID: ")
recovery_email = input("Enter your recovery email: ")

print(f"Gmail Registration: {gmail_id} created by {name} with recovery email {recovery_email}")

# EXERCISE 2 :

def check_phone_verified(phone_verified):
    if phone_verified:
        print("Phone number verified")
    else:
        print("Phone number not verified - PLEASE CROSSCHECK")

check_phone_verified(True)
check_phone_verified(False)
