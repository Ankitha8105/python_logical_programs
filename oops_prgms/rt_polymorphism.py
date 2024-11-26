class Animal:
    
    def make_sound(self):
        pass
    def eat(self):
        pass
    
class Dog(Animal):
    
    def make_sound(self):
        print("The dog sound like boww....")
        
    def eat(self):
        print("The dog eat pedigree")
        
dog_obj = Dog()
dog_obj.make_sound()
dog_obj.eat()