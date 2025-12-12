# greatest of four number.
a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number : "))
d = int(input("Enter the fourth number :"))

if(a>b and a>c and a>d):
    print("greatest number is a : ",a)

elif(b>a and b>c and b>d):
    print("greatest number is b : ",b)  

elif(c>a and c>b and c>d):
    print("greatest number is c :",c)

else:
    print("greatest number is d : ",d)
     
