# WAP to print multiplication table of n using for loop in reversed order

n = int(input(" enter the number : "))

for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")   # because 1 10   :: 1+10=11
                                        #           2 9    :: 2+9=11
                                        #           3 8    :: 3+8=11
                                        

