def store_contact(name,number,contacts={}):
    contacts[name.lower()] = number
    return contacts

def phone_book():
    contacts = {}
    while True:
        name = input("Enter name")
        number = input("Enter number")
        contacts = store_contact(name, number, contacts)
        user_choice = input("""
        Do you want to exit?
        1. Yes
        2. No
        """)
        if user_choice == "1":
            print(contacts)
            break

phone_book()