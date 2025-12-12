#creat a class for storing the information of programmer working form microsoft
class programmer:
    company = "microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("nilakshi",1500000,184148)
print(p.name ,p.salary ,p.pin ,p.company )        
