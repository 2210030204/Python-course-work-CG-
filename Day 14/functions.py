'''
def function_name(arg):
    #stmts
    return
function_name(para)
'''
def wish(name):
    print(f'Welcome to python course {name}')
wish('ram')
wish('raju')
wish('rani')

'''OUTPUT:
Welcome to python course ram
Welcome to python course raju
Welcome to python course rani
'''

def iseven(num):
    if num%2==0:
        return f"{num}-Even Number"
    else:
        return f"{num}-Odd number"
print(iseven(12))
print(iseven(13))




def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=1
        return fact
num=int(input("Enter the number:"))
print("Factorial:",factorial(num))

    


def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num}-Not Prime number"
    return f"{num}-Prime number"
num=int(input("enter the number:"))
print(isprime(num))
        


def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("pwd:",pwd)
display('ajay','ajay@gmail.com','123@a')
display('ajay@gmail.com','ajay','123@a')
display('ajay','123','ajay@gmail.com')






def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("pwd:",pwd)
display(name='ajay',email='ajay@gmail.com',pwd='123@a')
display(email='ajay@gmail.com',name='ajay',pwd='123@a')
display(name='ajay',pwd='123',email='ajay@gmail.com')



def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("pwd:",pwd)
display('ajay','ajay@gmail.com','123@a')
display('ajay@gmail.com','ajay')
