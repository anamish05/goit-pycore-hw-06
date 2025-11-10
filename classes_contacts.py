from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # class for the saving contact name
    def __init__(self, value):
         if not value: 
            raise ValueError("Please enter the name, it can't be empty")
         super().__init__(value)  # assign name, from Field class

class Phone(Field):
    # class for saving phone number with the format validation (10 digits)
    def __init__(self,value):
        self.check_format(value)
        super().__init__(value)

    def check_format(self,value):
        if not value.isdigit() or len(value)!=10:
            raise ValueError("Phone number must contain 10 digits")

class Record:
    # class for saving contact records
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self,phone):
        # to add new phone number
        self.phones.append(Phone(phone)) 

    def remove_phone(self,phone):
        # to delete phone number
        for p in self.phones:
             if p.value==phone:
                  self.phones.remove(p)
                  return True
        return False

    def edit_phone(self,old_phone,new_phone):
        # to edit phone number - replace old with new
        for i, p in enumerate(self.phones):
             if p.value==old_phone:
                  self.phones[i]=Phone(new_phone)
                  return True
        return False

    def find_phone(self,phone):
        # return phone if phone found
        for p in self.phones:
             if p.value==phone:
                  return p
        return None
                   
           

class AddressBook(UserDict):
    # class for saving and managing the contacts
    def add_record(self, record):
         self.data[record.name.value]=record

    def find(self, name):
         return self.data.get(name)
     
    def delete(self,name):
         if name in self.data:
             del self.data[name]


# testing the contact book
if __name__=="__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону в записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
