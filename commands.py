from record import Record
from classes import Phone, Birthday
from addressbook import AddressBook

 #Decorators for the errors handling
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Not correct arguments"
        except KeyError:
            return "No such contact found"
        except IndexError:
            return "Please add argument"
        except Exception as e:
            return f"Unexpected error: {e}"
    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def remove_phone(args, book:AddressBook):
    # to delete phone number of a contact
    name, phone = args
    record=book.find(name)
    if record:
        for p in record.phones:
            if p.value==phone:
                if len(record.phones)>1:
                    record.phones.remove(p)
                    return f"Phone deleted for contact {name}"
                else: 
                    return "Contact must have at least one phone number"
            return f"Contact {name} has no number {phone}"
    else:
        raise KeyError

@input_error
def edit_phone(args, book:AddressBook):
    # to edit phone number of a contact - replace old with new
    name, old_phone, new_phone = args
    record=book.find(name)
    if record:
        for i, p in enumerate(record.phones):
            if p.value==old_phone:
                record.phones[i]=Phone(new_phone)
                return f"Phone number changed for contact {name} from {old_phone} to {new_phone}"
        return f"Contact {name} does not have phone number {old_phone}"
    else:
        raise KeyError

@input_error
def add_birthday(args, book:AddressBook):
    #to add birthday date for a contact
    name, birthday = args
    record=book.find(name)
    if record:
        record.birthday=Birthday(birthday)
        return f"Birthday added for contact {name}"
    else:
        raise KeyError

@input_error
def show_birthday(args, book:AddressBook):
    #to show birthday of a contact
    name=args[0]
    record=book.find(name)
    if record:
        if record.birthday:
            return f"Contact: {name},\nBirthday: {record.birthday.value.strftime("%d.%m.%Y")}"
        return "Contact has no birthday date assigned"
    else:
        raise KeyError

@input_error
def show_phone (args, book: AddressBook):
    # to show phone numbers of a contact
    name=args[0]
    record=book.find(name)
    if record:
        return f"Contact name: {name},\nPhones: {'; '.join(p.value for p in record.phones)}"
    else: 
        raise KeyError
    
@input_error
def show_all(book:AddressBook):
    return book.get_all_contacts()

@input_error
def birthdays_next_week(book:AddressBook):
    if len(book.get_upcoming_birthdays())>0:
        return book.get_upcoming_birthdays()
    else:
        return "No upcoming birthdays next week"