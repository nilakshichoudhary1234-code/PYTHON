#WAP to find out whether a given post is talking about "harry" or not
post = input("enter the post :")
if("harry".upper() in post.upper()):      # we can write in any case capital ,lower or upper
    print("this post is talking about harry")
else:
    print("this post is not talking about harry")    
