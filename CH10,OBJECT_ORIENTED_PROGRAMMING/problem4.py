# add static method in problem 2
#class calculator which finds the square,cube and square root of a number.
class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square is {self.n*self. n}")  

    def cube(self):
        print(f"The square is {self.n*self. n*self.n}")

    def squareroot(self):
        print(f"The square is {self.n**1/2}")

    @staticmethod
    def hello():
        print("hello there!")              

a = Calculator(4)
a.square()
a.cube()
a.squareroot()
a.hello()

        
    
