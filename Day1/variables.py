# Gmail Registration System

def get_details():
    name = input("Enter Your Name: ")
    gmail_id = input("Enter Gmail ID: ")
    recovery_email = input("Enter Recovery Email: ")

    return name, gmail_id, recovery_email


def print_details(name, gmail_id, recovery_email):
    print("\n--- Gmail Registration Details ---")
    print(f"Name           : {name}")
    print(f"Gmail ID       : {gmail_id}")
    print(f"Recovery Email : {recovery_email}")


# Main Program
name, gmail_id, recovery_email = get_details()
print_details(name, gmail_id, recovery_email)
