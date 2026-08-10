# This is a phone book using dictionary

phone_book={}



while True:
    print("\nWelcome to Digital Phone Book")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All")
    print("4. Exit")

    choice = int(input("Enter your selection: "))

    if choice ==1:
        name = input("Enter Name: ").strip().title()
        phone_number = int(input("Enter Number: "))
        phone_book[name] = phone_number
        print(f"Contact {name} saved!")

    elif choice == 2:
        name = input("Enter name: ").strip().title()
        print(f"Number: {phone_book.get(name, 'Contact Not Found')}")

    elif choice == 3:
        print("\n All Contacts")
        for name,phone_number in phone_book.items():
            print(f"{name} : {phone_number}")

    elif choice == 4:
        break



    
