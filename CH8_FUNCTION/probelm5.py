# to print the pattern 
# ***
# **
# *     for n=3 by recursion

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1) 



pattern(3)

