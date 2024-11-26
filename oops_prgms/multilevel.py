class Switch:
    
    def turnon(self):
        print("The switch is turned on")
        
    def turnoff(self):
        print("The switch is turned off")
        
class Light(Switch):
    
    def turnon(self):
        print("The light is turned on")
        
    def turnoff(self):
        print("The light is turned off")
        
class Fan(Switch):
    
    def turnon(self):
        print("The fan is turned on")
        
    def turnoff(self):
        print("The fan is turned off")
        
class Person(Light,Fan):
    
    def working(self):
        print("Doing some work")
        
person_obj = Person()
person_obj.turnon()
person_obj.turnoff
print(Person.mro())