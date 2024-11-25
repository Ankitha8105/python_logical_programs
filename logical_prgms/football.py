class football:
    
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def get_age(self):
        print(f"{self.name} is {self.age} years")
        
    def get_height(self):
        print(f"{self.name} is {self.height}cm")
        
    def get_weight(self):
        print(f"{self.name} weighs {self.weight}kg")
        
football = football('David Jones',25,175,75)
football.get_age()
football.get_height()
football.get_weight()
        