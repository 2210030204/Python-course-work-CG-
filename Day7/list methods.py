Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4]
>>> m=[5,6,7,8]
>>> l+m
[1, 2, 3, 4, 5, 6, 7, 8]
>>> l*4
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> l=[10,20,30,40,50]
>>> l[4]
50
>>> l[2]
30
>>> l[0]
10
>>> l[-1]
50
>>> l[-3]
30
>>> l[-5]
10
>>> l
[10, 20, 30, 40, 50]
>>> l[:3]
[10, 20, 30]
>>> l[3:]
[40, 50]
>>> l[1:4]
[20, 30, 40]
>>> l[::-1]
[50, 40, 30, 20, 10]
>>> l[-1:-4:-1]
[50, 40, 30]
>>> l[-3::-1]
[30, 20, 10]
>>> 20 in l
True
>>> 40 in l
True
>>> 70 not in l
True
>>> 10 in l
True
80 in l
False
id(l)
2415754856384
l[1]
20
l[1]=70
l
[10, 70, 30, 40, 50]
id(l)
2415754856384
l[4]=100
l
[10, 70, 30, 40, 100]
l.append(120)
l
[10, 70, 30, 40, 100, 120]
l.append(400)
l
[10, 70, 30, 40, 100, 120, 400]
l.insert(1,60)
l
[10, 60, 70, 30, 40, 100, 120, 400]
l.insert(4,50)
l
[10, 60, 70, 30, 50, 40, 100, 120, 400]
l.extend([80,90,110])
l
[10, 60, 70, 30, 50, 40, 100, 120, 400, 80, 90, 110]
l.pop()
110
l
[10, 60, 70, 30, 50, 40, 100, 120, 400, 80, 90]
l.pop()
90
l
[10, 60, 70, 30, 50, 40, 100, 120, 400, 80]
l.pop(3)
30
l
[10, 60, 70, 50, 40, 100, 120, 400, 80]
l.pop(1)
60
l
[10, 70, 50, 40, 100, 120, 400, 80]
l.remove(100)
l
[10, 70, 50, 40, 120, 400, 80]
l.remove(400)
l
[10, 70, 50, 40, 120, 80]
del l[1]
l
[10, 50, 40, 120, 80]
del l[2]
l
[10, 50, 120, 80]
l.clear()
l
[]
id(l)
2415754856384
l=[100,20,89,45,30,300,45]
l
[100, 20, 89, 45, 30, 300, 45]
sorted(l)
[20, 30, 45, 45, 89, 100, 300]
l.sort()
l
[20, 30, 45, 45, 89, 100, 300]
min(l)
20
max(l)
300
l
[20, 30, 45, 45, 89, 100, 300]
l.reverse()
l
[300, 100, 89, 45, 45, 30, 20]
l.sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    l.sorted(reverse=True)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
sorted(l,reverse=True)
[300, 100, 89, 45, 45, 30, 20]
l.index(120)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    l.index(120)
ValueError: list.index(x): x not in list
l.index(100)
1
lindex(20)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    lindex(20)
NameError: name 'lindex' is not defined
l.index(20)
6
l.count(30)
1
l.count)100)
SyntaxError: unmatched ')'
l.count(100)
1
l
[300, 100, 89, 45, 45, 30, 20]
m=l
m
[300, 100, 89, 45, 45, 30, 20]
m.append(700)
m
[300, 100, 89, 45, 45, 30, 20, 700]
l
[300, 100, 89, 45, 45, 30, 20, 700]
n=l.copy()
n
[300, 100, 89, 45, 45, 30, 20, 700]
n.append(800)
n
[300, 100, 89, 45, 45, 30, 20, 700, 800]
l
[300, 100, 89, 45, 45, 30, 20, 700]
len(l)
8
sum(l)
1329
any([1,2,3,0,5,5,0,0,0,0])
True
all([1,2,4,5,5,0,0,0,0])
False
