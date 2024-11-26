from abc import ABC,abstractmethod
class Univeristy(ABC):
    
    @abstractmethod
    def conduct_exam(self):
        pass
    @abstractmethod
    def give_registartion_num(self):
        pass
    
class College(Univeristy):
    
    def conduct_exam(self):
        print("The college conducting exams")
        
    def give_registartion_num(self):
        print("The give USN to students")
        
college_obj = College()
college_obj.conduct_exam()
college_obj.give_registartion_num()