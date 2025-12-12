# to calculate the factorial of a given number using for loop
n = int(input("enter the number :"))

i=1
fact = 1
while(i<=n):
    fact = fact*i
    i+=1
    
print(f"The factorial of {n} is {fact}")

    