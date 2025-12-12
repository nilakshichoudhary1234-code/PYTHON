#create an empty set
#allow 4 friends to enter their favourite language as value and use keys as their names 
# allow that names are unique
d={}
name  = input("enter friend name: ")
lang = input("enter language name: ")
d.update({name:lang})

name  = input("enter friend name: ")
lang = input("enter language name: ")
d.update({name:lang})

name  = input("enter friend name: ")
lang = input("enter language name: ")
d.update({name:lang})

name  = input("enter friend name: ")
lang = input("enter language name: ")
d.update({name:lang})

print(d)