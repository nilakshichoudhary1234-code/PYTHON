class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[0]

e= Employee()
e.a = 45

e.name="Harry"
print(e.name)

e.show()

#7:42:10