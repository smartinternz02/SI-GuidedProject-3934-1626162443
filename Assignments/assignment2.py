a=str(input("name:"))
b=int(input("age:"))
if(a=="alice"):
    print("hi there alice")
    sys.exit()

elif(b<=12):
    print("you're not Alice,kiddo")
    sys.exit()
elif(b>=100):
    print("you're not Alice,granny")   
    sys.exit()  
elif(b>=2000):
    print("unlike you,Alice is not an undead,immortal vampire.")
    sys.exit()
