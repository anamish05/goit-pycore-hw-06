from collections import UserDict
from datetime import datetime as dt
from datetime import timedelta
from record import Record


class AddressBook(UserDict):
    # class for saving and managing the contacts
    def add_record(self, record:Record):
         self.data[record.name.value]=record

    def find(self, name):
         return self.data.get(name)
     
    def delete(self,name):
         if name in self.data:
             del self.data[name]

    def get_upcoming_birthdays(self):
        current_date=dt.today().date()
        next_week=current_date+timedelta(days=7)
        upcoming_bd=[]
        for name, record in self.data.items():
            bd_this_year=record.birthday.value.replace(year=current_date.year)
            if bd_this_year<current_date:
                bd_this_year=bd_this_year.replace(year=current_date.year+1)
                if current_date<=bd_this_year<=next_week:
                    congrat_date=bd_this_year
                    if congrat_date.weekday()==5:
                        congrat_date+=timedelta(days=2)
                    elif congrat_date.weekday()==6:
                        congrat_date+=timedelta(days=1)
                    upcoming_bd.append({"Name":name," Congratulation_date":congrat_date.strftime("%d.%m.%Y")})
        return upcoming_bd
    
    def get_all_contacts (self):
    # to show all contacts of a book
        if not self.data:
            return "Contact book is empty"

        result=[]
        for record in self.data.values():
                result.append(str(record))
        return "\n".join(result)