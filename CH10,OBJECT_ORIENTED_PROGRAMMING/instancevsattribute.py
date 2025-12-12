class employee:
   # name ="nilakshi"
    language ="python"# this is the class attribute
    salary = 1200000


nilakshi = employee()
nilakshi.language = "javascript"# this is the instance attribute.
print( nilakshi.salary,nilakshi.language)

#instance attribute has more priority than class attribute.