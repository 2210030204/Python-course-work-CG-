'''
#SYNTAX
var=lambda arg: exp'''

add=lambda a,b: a+b
print(add(12,13))
print(add(45,87))

'''#OUTPUT:
25
132'''

wish =lambda name:f'welcome to the course: {name}'
print(wish('Ajay'))
print(wish('ram'))

'''#OUTPUT:
welcome to the course: Ajay
welcome to the course: ram'''

gst = lambda amount: amount + amount * 0.18
print(gst(12000))
print(gst(82422))
print(gst(80843))

'''#OUTPUT:
14160.0
97257.95999999999
95394.74'''


greatest=lambda a,b: a if a>b else b
print(greatest(10,19))
print(greatest(120,1349))
print(greatest(134,239))

'''#OUTPUT
19
1349
239'''


iseven=lambda a: f"{a}-Even number" if a%2==0 else f"{a}-odd number"
print(iseven(2))
print(iseven(23))
print(iseven(268))

'''#OUTPUT:
2-Even number
23-odd number
268-Even number'''


bill=lambda charge: charge if charge>99 else charge+30
print(bill(56))
print(bill(156))
print(bill(236))
'''#OUTPUT:
86
156
236'''

login=True
instock=True
status = lambda login,instock: ("YOU can buy the product" if instock else "Product out of stock") if login else "Login to buy the products"
print(status(login,instock))
'''#OUTPUT:
YOU can buy the product'''


l=[1,2,3,4,5,6,7]
res=list(map(lambda i:i**3,l))
print(res)

'''#OUTPUT:
[1, 8, 27, 64, 125, 216, 343]'''

names=['ajay','ram','bunny']
t=list(map(lambda i:i.title(),names))
print(t)

'''#OUTPUT:
['Ajay', 'Ram', 'Bunny']'''

l=[1,2,3,4,5,6,7]
res=list(filter(lambda i:i%2==0,l))
print(res)

'''#OUTPUT:
[2, 4, 6]'''


l=[1,2,3,4,5,6,7]
res=list(filter(lambda i:i>5,l))
print(res)

'''#OUTPUT:
[6,7]'''


from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
s=reduce(lambda sum,i: sum+i,l)
p=reduce(lambda pro,i: pro*i,l)
print(s,p)

'''#OUTPUT:
78 479001600'''


from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
m=reduce(lambda max,i: max if max>i else i,l)
mi=reduce(lambda max,i: max if max<i else i,l)

''' #OUTPUT:
12
1'''


d={'Ajay':50,"ram":39,"suma":90,"deeru":45}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))

'''#OUTPUT:
{'Ajay': 50, 'deeru': 45, 'ram': 39, 'suma': 90}
{'ram': 39, 'deeru': 45, 'Ajay': 50, 'suma': 90}
{'suma': 90, 'ram': 39, 'deeru': 45, 'Ajay': 50}
{'suma': 90, 'Ajay': 50, 'deeru': 45, 'ram': 39}'''

