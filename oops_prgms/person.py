import datetime
class Person:
    
    def __init__(self,name,country,date):
        self.name = name
        self.country = country
        self.date_birth = date
        
    def cal_age(self):
        today = datetime.date.today()
        age = today.year - self.date_birth.year
        return age
    

Person_obj = Person("Disha","New York",datetime.date(2001,12,19))
print(f"The age of person is {Person_obj.cal_age()}")
        
         