Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t
()
t=(1,1,12,3,4,5)
t
(1, 1, 12, 3, 4, 5)
t=(1,'ajay',4.7,2,3,[])
t
(1, 'ajay', 4.7, 2, 3, [])
t=(10,20,30,40,50)
t
(10, 20, 30, 40, 50)
h=(90,80,70)
t+h
(10, 20, 30, 40, 50, 90, 80, 70)
t*4
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t[1]
20
t[4]
50
t[22]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t[22]
IndexError: tuple index out of range
t[2]
30
t[-2]
40
t[-3]
30
t[-1]
50
t[:3]
(10, 20, 30)
t[3:]
(40, 50)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::2]
(10, 30, 50)
t[::-1]
(50, 40, 30, 20, 10)
t[-1:-4:-1]
(50, 40, 30)
10 in t
True
30 in t
True
60 not in t
True
10 not in t
False
len(t)
5
sorted(t)
[10, 20, 30, 40, 50]
min(t)
10
>>> max(t)
50
>>> sum(t)
150
>>> t.count(10)
1
>>> t.index(10)
0
>>> t=1,2,3,4,5,6,7
>>> t
(1, 2, 3, 4, 5, 6, 7)
>>> a,b,c=(1,2,3)
>>> a
1
>>> b
2
>>> c
3
>>> a=(1,2,4)
>>> a
(1, 2, 4)
>>> x,y,z=a
>>> x
1
>>> y
2
>>> z
4
>>> t=(1,2,3,[4,5,6],7,8)
>>> t
(1, 2, 3, [4, 5, 6], 7, 8)
>>> t[2]
3
>>> t[4]
7
>>> t[8]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    t[8]
IndexError: tuple index out of range
>>> t[3]
[4, 5, 6]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
