import math
class Circle:
    
    def __init__(self,radius):
        self.radius = radius
    
    def cal_area(self):
        print(f"The area of circle is {math.pi*math.pow(self.radius,2)}")
    
    def cal_peri(self):
        print(f"The perimeter of circle is {2*math.pi*self.radius}")
      
circle = Circle(5)
circle.cal_area()
circle.cal_peri()  
num=[1,2,3,4,5]
l=[]
for i in num:
    if i%2 != 0:
        l.append(i)
print("Odd:",l)

j=[i for i in num if i%2!=0]
print(j)