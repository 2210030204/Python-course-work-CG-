Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={1,2,3,4}
s
{1, 2, 3, 4}
s=set()
s
set()
s={1,1,1,,1,1}
SyntaxError: invalid syntax
s={1,1,1,1,1}
s
{1}
s={3,56,75,1,90,10,455}
s
{1, 3, 90, 455, 56, 10, 75}
s=set()
s.add(1)
s
{1}
s.add(156.98)
s
{1, 156.98}
s.add("kjy")
s
{1, 'kjy', 156.98}
s.add(True)
s
{1, 'kjy', 156.98}
1 in s
True
2 in s
False
False not in s
True
a={1,2,3,5,6,8,10}
a
{1, 2, 3, 5, 6, 8, 10}
b={6,7,8,9}
a.union(b)
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a|b
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.intersect(b)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.intersect(b)
AttributeError: 'set' object has no attribute 'intersect'. Did you mean: 'intersection'?
a.intersection(b)
{8, 6}
>>> a&b
{8, 6}
>>> a-b
{1, 2, 3, 5, 10}
>>> a^b
{1, 2, 3, 5, 7, 9, 10}
>>> a
{1, 2, 3, 5, 6, 8, 10}
>>> a<={1}
False
>>> a>={1}
True
>>> a<{1,2,3,4,5,6,7,8,9}
False
>>> a<={1,2,3,4,5,6,7,8}
False
>>> a.isdidjoint(b)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.isdidjoint(b)
AttributeError: 'set' object has no attribute 'isdidjoint'. Did you mean: 'isdisjoint'?
>>> a.isdisjoint(b)
False
>>> a.isdisjoint(10,20)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.isdisjoint(10,20)
TypeError: set.isdisjoint() takes exactly one argument (2 given)
>>> a
{1, 2, 3, 5, 6, 8, 10}
>>> a.add(17)
>>> a
{1, 2, 3, 17, 5, 6, 8, 10}
>>> a.update({11,12,13})
>>> a
{1, 2, 3, 5, 6, 8, 10, 11, 12, 13, 17}
>>> a.remove(10)
>>> a
{1, 2, 3, 5, 6, 8, 11, 12, 13, 17}
>>> a.discard(10)
>>> a
{1, 2, 3, 5, 6, 8, 11, 12, 13, 17}
>>> a.clear()
>>> a
set()
