# student has passed or not if it requires a total of 40% and atleast 33% in each subject to pass.
a = int(input("enter the first subject marks : "))
b = int(input("enter the second subject marks :"))
c = int(input("enter the third subject marks : "))

total_percentage = (((a+b+c)/300)*100)

if(total_percentage>=40 and a>=33 and b>=33 and c>=33):
    print("you passed the exam",total_percentage)

else: 
    print("you failed the exam",total_percentage)


