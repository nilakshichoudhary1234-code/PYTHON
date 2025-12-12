# to print pattern  *
#                   **
#                   ***  for n=3

n = int(input("enter the number :"))

for i in range(1,n+1):
    print("*"*i,end ="")
    print(" "*(n-1),end="")
    print("")