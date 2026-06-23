d={'sugar':40,'salt':20,'coooking':80,'chilli':60}
res=dict(map(lambda i: (i[0],i[1]+i[1]*0.18),d.items()))
res1=dict(map(lambda i: (i[0],i[1]-i[1]*0.5),d.items()))
print(res)
print(res1)


'''#OUTPUT:
{'sugar': 47.2, 'salt': 23.6, 'coooking': 94.4, 'chilli': 70.8}
{'sugar': 20.0, 'salt': 10.0, 'coooking': 40.0, 'chilli': 30.0}'''



d={'sugar':40,'salt':20,'coooking':80,'chilli':60}
res=dict(filter(lambda i:i[1]>50,d.items()))
res1=dict(filter(lambda i:i[1]<50,d.items()))
print(res)
print(res1)


'''#OUTPUT:
{'coooking': 80, 'chilli': 60}
{'sugar': 40, 'salt': 20}'''

