'''import sys
print(sys.argv)
print(sys.path)
print(sys.version)
print("Before exit")
sys.exit()
print("After exit")'''




import platform
print(platform.system(),platform.release(),platform.processor())




import math
print(math.pi)
print(math.e)
print(math.sqrt(25))
print(math.pow(2,5))
print(math.ceil(12.3))
print(math.ceil(12.000000))
print(math.ceil(12.999999))
print(math.ceil(12.6))
print(math.floor(12.3))
print(math.floor(12.00000))
print(math.floor(12.9999))
print(math.floor(12.6))
print(round(20.3))
print(round(20.7))

import math
print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(8,25))
print(math.log(10,10))
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))
print(math.degrees(20))
print(math.radians(25))



import random
random.seed(4)
print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))
l=['python','c','c++','java','html']
print(random.choice(l))
print(random.choices(l,k=3))
s='rps'
print(random.choice(s))
print(l)
random.shuffle(l)
print(l)


import collections
s='python programing language'
print(collections.Counter(s))
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


import collections
s='python programing language'
d=collections.defaultdict(int)
for i in s:
    d[i]+=1
print(d)


import collections
l=collections.deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()
print(l)

import itertools 
print(list(itertools.combinations('ABCD', 2)))
print(list(itertools.combinations('ABCD', 2)))






