"""
Simple Contact Book
Add, view, and search contacts.
"""

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts.append({'name': name, 'phone': phone})
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    search = input("Enter name to search: ").lower()
    found = False
    for contact in contacts:
        if search in contact['name'].lower():
            print(f"Found: {contact['name']} - {contact['phone']}")
            found = True
    if not found:
        print("No matching contact found.")

if __name__ == "__main__":
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
