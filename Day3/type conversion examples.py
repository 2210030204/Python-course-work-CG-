Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
a
10
type(a)
<class 'int'>
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=2.0
int(b)
2
str(b)
'2.0'
complex(b)
(2+0j)
bool(b)
True
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
list(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
c='python'
int(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(c)
ValueError: invalid literal for int() with base 10: 'python'
float(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(c)
ValueError: could not convert string to float: 'python'
list(c)
['p', 'y', 't', 'h', 'o', 'n']
tuple(c)
('p', 'y', 't', 'h', 'o', 'n')
set(c)
{'h', 't', 'y', 'p', 'o', 'n'}
dict(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(c)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
complex(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex(c)
ValueError: complex() arg is a malformed string
bool(c)
True
a=['a','b','c']
int(a)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'list'
str(a)
"['a', 'b', 'c']"
bool(a)
True
complex(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not list
tuple(a)
('a', 'b', 'c')
dict(a)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
set(a)
{'b', 'a', 'c'}
a=("a","b","c")
int(a)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
\
float(a)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(a)
"('a', 'b', 'c')"
complex(a)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not tuple
bool(a)
True
list(a)
['a', 'b', 'c']
set(a)
{'b', 'a', 'c'}
dict(a)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
a={"a","b","c"}
int(a)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(a)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'set'
str(a)
"{'b', 'a', 'c'}"
bool(a0
     complex(a)
     
SyntaxError: '(' was never closed
bool(a)
     
True
complex(a)
     
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not set
list(a)
     
['b', 'a', 'c']
tuple(a)
     
('b', 'a', 'c')
dict(a)
     
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
a={'name':'Ajay','age':20}
     
int(a)
     
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(a)
     
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'dict'
str(a)
     
"{'name': 'Ajay', 'age': 20}"
bool(a)
     
True
complex(a)
     
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not dict
list(a)
     
['name', 'age']
tuple(a)
     
('name', 'age')
set(a)
     
{'age', 'name'}
a=3+4j
     
int(a)
     
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
...      
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> str(a)
...      
'(3+4j)'
>>> list(a)
...      
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    list(a)
TypeError: 'complex' object is not iterable
>>> tuple(a)
...      
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable
>>> dict(a)
...      
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    dict(a)
TypeError: 'complex' object is not iterable
>>> set(a)
...      
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    set(a)
TypeError: 'complex' object is not iterable
>>> bool(a)
...      
True
>>> a=True
...      
>>> str(a)
...      
'True'
>>> int(a)
...      
1
>>> complex()
...      
0j
