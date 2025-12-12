# file contain a word "DONKEY " multuple times .you need to write a program which replace this word with ##### by updating the same file 
word = "donkey"

with open("file2.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word,"#####")

with open("file2.txt","w") as f:
    f.write(contentNew)


