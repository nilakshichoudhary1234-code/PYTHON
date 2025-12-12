class Employee:
    company ="ITC"
    name="default name"
    def show(self):
        print(f"the name is {self.name} and the company is {self.company}")

class coder:
    language="python"
    def printLanguages(self):
        print(f"out of all the languages here is your language: {self.language}")

class Programmer(Employee,coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()





