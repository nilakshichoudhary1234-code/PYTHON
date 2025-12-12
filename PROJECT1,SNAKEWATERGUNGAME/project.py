import random    #so that computer provide any eandom number from three of them
'''
1 for snake 
-1 for water 
0 for gun

'''
computer = random.choice([-1,0,1]) 
youstr = input("Enter your choice : ")  # to enter our choice
youDict ={"s":1,"w":-1,"g":0 }
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youstr]

#by now we have two numbers(variable),you and computer


print(f"You choose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")



if(computer == you):
    print("Its a Draw")

else:

   if(computer ==-1 and you ==1):
    print("You Win!")

   elif(computer ==-1 and you ==0):
    print("You Lose!") 

   elif(computer ==1 and you ==-1):
    print("You Lose!")

   elif(computer ==1 and you ==0):
    print("You Win")            

   elif(computer ==0 and you ==1):
    print("You Lose!")

   elif(computer ==0 and you ==-1):
    print("You Win")            

   else:
    print("something went wrong")

# another way 
# if(comouter - you )== -1 or (computer-you == 2):
        # print ("you lose ")
# else: 
#     print("you win")    




