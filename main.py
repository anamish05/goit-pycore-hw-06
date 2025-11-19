from classes import Name, Birthday, Phone
from record import Record
from addressbook import AddressBook
from commands import add_contact, remove_phone, edit_phone, add_birthday, show_birthday, show_phone, show_all, birthdays_next_week


#function for parsing an user input
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change-phone":
            print(edit_phone(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command=="remove-phone":
            print(remove_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays_next_week(book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main() 