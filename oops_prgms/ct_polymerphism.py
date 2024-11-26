class Calculator:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        print(f"the sum of two numbers is {self.a+self.b}")
        
    def add(self,a,b):
        print(f"the sum of two numbers is {a+b}")
        
    def add(self,b,a):
        print(f"the sum of two numbers is {a+b}")
        
calculator_obj = Calculator(2,3)
calculator_obj.add(2,7)
calculator_obj.add(8,5)