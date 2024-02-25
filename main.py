'''This module implements functionality for a CLI Bot.'''


def parse_input(user_input):
    '''"This function parses user-entered arguments and returns them.'''

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def get_all(contacts):
    '''This function returns all user data.'''

    for name, phone in contacts.items():
        print(f'{name:10} | {phone:15}')


def add_contact(args, contacts):
    '''This function adds a new user to the storage.'''

    if len(args) != 2:
        print("Invalid number of arguments. "
              "Please provide both name and phone number.")
        return
    name, phone = args
    contacts[name] = phone
    print("Contact added.")


def change_contact(args, contacts):
    '''This function changes the user's phone number in the storage.'''

    if len(args) != 2:
        print("Invalid number of arguments. "
              "Please provide both name and phone number.")
        return
    name, phone = args
    user_name = name.capitalize()
    contacts[user_name] = phone
    print("Contact changed.")


def get_phone_contact(args, contacts):
    '''This function returns the user's phone number.'''

    if len(args) != 1:
        print("Invalid number of arguments. Please provide a name.")
        return
    [name] = args
    user_name = name.capitalize()
    if user_name not in contacts:
        print("Contact not found.")
        return
    print(contacts[user_name])


def main():
    '''Primary function for interacting with the user via the command line.'''

    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command == "all":
            get_all(contacts)
        elif command == "add":
            add_contact(args, contacts)
        elif command == "change":
            change_contact(args, contacts)
        elif command == "phone":
            get_phone_contact(args, contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
