Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
type(a)
<class 'int'>
t= 999.99
type(t)
<class 'float'>
c = 12+8j
type(c)
<class 'complex'>
s='python'
type(s)
<class 'str'>
>>> s='python'
>>> s='java'
>>> s
'java'
>>> s='python'
>>> id(s)
2373157568160
>>> s='java'
>>> id(s)
2373165838000
>>> l=[1,2,3,4]
>>> id(l)
2373202772288
>>> l.append(50)
>>> l.append(60)
>>> l
[1, 2, 3, 4, 50, 60]
>>> id(l)
2373202772288
>>> l=['Ranjithkumar','aanchala']
>>> l
['Ranjithkumar', 'aanchala']
>>> l=['Ranjithkumar','paanchala']
>>> l
['Ranjithkumar', 'paanchala']
>>> k=1,2,3,4)
SyntaxError: unmatched ')'
>>> k=(1,2,3,4)
>>> k
(1, 2, 3, 4)
>>> type(k)
<class 'tuple'>
>>> a=(1,2,3,4)
>>> type(s)
<class 'str'>
>>> a={1,2,3,4}
>>> type(s)
<class 'str'>
>>> type(a)
<class 'set'>
>>> s=set{}
SyntaxError: invalid syntax
>>> s=set()
>>> s={1,2,3,4,54,65,45,45}
>>> s
{1, 2, 3, 4, 65, 54, 45}
