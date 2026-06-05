Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = '    hello    world     '
>>> s.strip()
'hello    world'
>>> s.lstrip()
'hello    world     '
>>> s.rstrip()
'    hello    world'
>>> s = 'strings.py'
>>> s
'strings.py'
>>> s.startswith('gfh')
False
>>> s.endswith('py')
True
>>> s.endswith('js')
False
>>> 'sdfyui'.isalpha()
True
>>> 'hekgvfkajbskbkKJIHBJKHBHJLKB'.isalpha()
True
>>> 'sai@1234'.isalpha()
False
>>> 'bfwtg'.islower()
True
>>> 'UIHGHIGLKJHBHJ'.isupper()
True
>>> ' '.isspace()
True
>>> 'hello      '.isspace()
False
>>> 'Py prg Lan'.istitle()
False
>>> 'py_[ython'.isidentifier()
False
>>> 'py_python'.isidentifier()
True
>>> l = []
>>> l = list()
>>> type(l)
<class 'list'>
>>> l = [1,2,3,4]
>>> m = [7,5,4,3]
>>> l+m
[1, 2, 3, 4, 7, 5, 4, 3]
>>> l*4
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> l = [10,20,30,40,50]
>>> l[4]
50
>>> l[2]
30
>>> l[0]
10
>>> l[1]
20
>>> l[-1]
50
>>> l[-3]
30
>>> 
>>> l[1]=70
>>> l
[10, 70, 30, 40, 50]
>>> l[4]=100
>>> l
[10, 70, 30, 40, 100]
>>> l.append(120)
>>> l
[10, 70, 30, 40, 100, 120]
>>> l.append(400)
>>> l
[10, 70, 30, 40, 100, 120, 400]
>>> l.insert(4,50)
>>> l
[10, 70, 30, 40, 50, 100, 120, 400]
>>> l.extend([80,90,110])
>>> l
[10, 70, 30, 40, 50, 100, 120, 400, 80, 90, 110]
>>> l.pop(110)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    l.pop(110)
IndexError: pop index out of range
>>> l.pop()
110
>>> 
>>> l
[10, 70, 30, 40, 50, 100, 120, 400, 80, 90]
>>> l.pop(3)
40
>>> del l[1]
>>> l
[10, 30, 50, 100, 120, 400, 80, 90]
>>> l.clear()
>>> l
[]
>>> l = [23,34,12,11,234,433,333,222,111,1,11]
>>> sorted(l)
[1, 11, 11, 12, 23, 34, 111, 222, 234, 333, 433]
>>> 
>>> l.sort()
>>> l
[1, 11, 11, 12, 23, 34, 111, 222, 234, 333, 433]
>>> min(l)
1
>>> max(l)
433
>>> l.sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    l.sorted(reverse=True)
AttributeError: 'list' object has no attribute 'sorted'
>>> sorted(l,reverse = True)
[433, 333, 234, 222, 111, 34, 23, 12, 11, 11, 1]
>>> l.index(120)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    l.index(120)
ValueError: 120 is not in list
>>> l.index(444)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    l.index(444)
ValueError: 444 is not in list
>>> l.clear()
>>> l
[]
>>> l = [400,200,120,100,70,50,33,30,10,700]
>>> len(l)
10
>>> sum(l)
1713
>>> any([1,2,4,5,5,0,0,0,0,0])
True
>>> all([1,2,4,5,5,0,0,0,0,0])
False
>>> 