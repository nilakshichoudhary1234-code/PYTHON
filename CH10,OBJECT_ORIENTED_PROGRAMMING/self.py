class employee:
    language = "python"
    salary = 1200000

    def getInfo(self):
        print(f"The languge is {self.language}. The salary is {self.salary}")
    
    def greet(self):
        print("Great job")    


harry = employee()
harry.language ="javascript"
harry.getInfo()
harry.greet()
#employee.getInfo(harry)
