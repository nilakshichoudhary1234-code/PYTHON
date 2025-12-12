#dictionary methods marks 
d={} #empty dictionary

marks ={
    "harry" : 100,
    "shuvam" : 56,
    "rohan" : 56,
    0 : "harry"
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"harry" :99 , "pari" :100}) # it also udate as well as add the new dictionary
print(marks)

print(marks.get("rohan")) # in get option if the keyword doesnot exists it will return none

print(marks["rohan"]) # in this case if the key doesnot exist then it will show error
