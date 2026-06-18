#FOR LOOP WITH ELSE
n= int(input())
passw=123
for i in range(5):
    if n==passw:
        print("phone unlocked")
        break
    else:
        print("Incorrect")
else:
    print("try after 60 seconds")



n=int(input())
l=[2,3,5,6,7,8,99]
for i in range(len(l)):
    if l[i]==n:
        print(f"{n} is found at index-{i}")
        break
else:
    print("number not found")




password=input("Enter the password:")
if len(password)>=8:
    s=set()
    for i in password:
       if i.isupper():
           s.add("u")
       elif i.islower():
           s.add("l")
       elif i.isdigit():
           s.add("d")
       else:
           s.add("s")
    if len(s)==4:
        print("strong password")
    else:
        print("weak password")
        
else:
    print("Weak Password")


#ASSERTION

status=None
assert status!=None,"you need to update the status"
print(status)


name="abs"
batch=55
assert(name!=None and batch!=None and age!=None),"You need to update the age"
print(name,batch,age)



