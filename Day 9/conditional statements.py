'''conditionalstatements
 simple if
 if-else
 if-elif-else
 nested if
 '''

s='python'
if 'python' in s:
    print('python found')
if s[0]=='p':
    print("string is starting with p:")




data=('abc','1234')
username,password=input("Enter the username and password").split()
if (data==username,password):
    print("Login Sucessfull")
else:
    print("Invalid")


#if-else-elif
n=int(input("Enter the number:"))
if n>0:
    print("positive")
elif n<0:
    print("Negative")
else:
    print("Zero")


#nested if
products={'laptops':0,'mouse':10,'charger':5,'phones':30,'keyboard':0}
product=input("Enter the product")
if product in products:
    if products[product]!=0:
        print(f"you can buy {products}")
    else:
        print("product out of stock")
else:
    print(f"product is not available")
