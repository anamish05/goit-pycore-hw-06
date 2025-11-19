import re
from datetime import datetime as dt


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
        
class Birthday(Field):
    # class for saving birthday with the format validation (dd.mm.yyyy)
    def __init__(self, value):
        if re.match(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$",value):
            if dt.strptime(value, "%d.%m.%Y").date() > dt.today().date():
                raise Exception("Birthday date cannot be the future")
            self.value = dt.strptime(value, "%d.%m.%Y").date() 
        else:
            raise Exception("Invalid date format. Use DD.MM.YYYY")


