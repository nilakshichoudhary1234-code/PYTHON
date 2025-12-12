class Employee:
    a = 1

    # to make to print 1 instead of 45 we will use class attribute
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

e = Employee()
e.a = 45

e.show()
