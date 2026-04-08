# Contact Book Application

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter addredd: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully.\n")

def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return

    print("Contact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")
    print()

def search_contact():
    search = input("Enter name or phone number to search: ")

    for name, details in contacts.items():
        if search == name or search == details["phone"]:
            print("Contact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")
            return

    print("Contact not found.\n")

def update_contact():
    name = input("Enter contact name to update: ")

    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")

        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        contacts[name]["address"] = address

        print("Contact updated successfully.\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.\n")
    else:
        print("Contact not found.\n")

def main():
    while True:
        print("Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
        
