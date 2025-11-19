from classes import Name, Phone, Birthday


class Record:
    # class for saving contact records
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday=None


    def __str__(self):
        return (f"Contact name: {self.name.value},\n"
                f"Phones: {'; '.join(p.value for p in self.phones)},\n"
                f"Birthday: {self.birthday.value.strftime("%d.%m.%Y") if self.birthday and self.birthday.value else 'NA'},\n"
                "--------------------------------------------------------")
    
   
    def add_phone(self, phone):
        # to add new phone number
        for p in self.phones:
            if phone==p.value:
                return "This phone number already exists"
        else:
            self.phones.append(Phone(phone))
            return f"Phone number added for contact {self.name}"
                   