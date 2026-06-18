'''#RECURSION
def func():
    if basecondition
        return
    func()'''
def func(num):
    if num ==0:
        return
    print(num,end=' ')
    func(num-1)
func(5)
    
'''#Output:
5 4 3 2 1'''



def func(num):
    if num ==0:
        return
    func(num-1)
    print(num,end=' ')
func(5)

'''#Output:
1 2 3 4 5 '''



def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(5))


'''#Output
15'''
def productofdigits(n):
    if n==0:
        return 1
    return n*productofdigits(n-1)
print(productofdigits(5))

'''#Output:
120'''


def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,4))
print(power(3,3))

'''#Output:
16
27'''


def reverseofstring(s,ind):
    if ind==0:
        return s[0]
    return s[ind]+reverseofstring(s,ind-1)
l="Python Programming"
print(reverseofstring(l,len(l)-1))

'''#Output:
gnimmargorP nohtyP
'''
