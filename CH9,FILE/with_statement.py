f=open("file.txt")

print(f.read())
f.close()

#to avoid writing the f close()
#the same can be written using with statement
with open("file.txt")as f:
    print(f.read())

#you dont have to explicitly close the file  
 
