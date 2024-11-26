class Shape:
    
    def cal_area(self):
        pass
    
    def cal_peri(self):
        pass
    
class Triangle(Shape):
    
    def __init__(self,b,h,side):
        self.base = b
        self.height = h
        self.side = side
    
    def cal_area(self):
        print(f"The area of circle is {0.5*self.base*self.height}")
    
    def cal_peri(self):
        print(f"The perimeter of triangle is {self.base+self.height+self.side}")
          
triangle_obj = Triangle(13,14,15)
triangle_obj.cal_area()
triangle_obj.cal_peri()