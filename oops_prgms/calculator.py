class Calculator:
    
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
     
    def add(self):
        print(f"the sum of two numbers is {self.num1+self.num2}")
      
    @classmethod  
    def mul(cls,a,b):
        print(f"The Multiplication of two numbers is {a*b}")
    
    @classmethod  
    def div(cls,a,b):
        if (b == 0):
            raise("Get Zero division error")
        else:
            print(f"The Division of 2 numbers is {a//b}")
            
calculator_obj = Calculator(2,5)
calculator_obj.add()
Calculator.mul(2,3)
Calculator.div(16,2)

