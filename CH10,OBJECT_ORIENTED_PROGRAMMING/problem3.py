# to create a class attribute a; create an object from it and set 'a' directly using object.a=o 
class demo:
    a=4

o=demo()
print(o.a)#print class attribute because instance attribute is not present 

o.a=0#instance attribute is set
print(o.a)#print the instance attribute because instance attribute is present   
print(demo.a)# print the class attribute 