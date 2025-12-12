# to calculate the grades of the students 
m =int( input("Enter the marks of the student :"))

if(m<=100 and m>90):
    print("excellent")

elif(m<=90 and m>80):
    print("grade : A")

elif(m<=80 and m>70):
    print("grade : B")

elif(m<=70 and m>60):
    print("grade : C"
          ) 
elif(m<=60 and m>50):
    print("grade : D")

else:
    print("grade : F")                   