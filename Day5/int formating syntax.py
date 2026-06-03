Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input()
ranjith
name
'ranjith'
name=input("Enter your name:")
Enter your name:ranjith
name
'ranjith'
age=input("Enter your agr:")
Enter your agr:21
age
'21'
type(age)
<class 'str'>
gpa=float(input("enter your gpa"))
enter your gpa7.3
gpa
7.3
type(gpa)
<class 'float'>
'ranjith ajay preetham eshwar.split(' ')
SyntaxError: unterminated string literal (detected at line 1)
'ranjith ajay preetham eshwar'.split(' ')
['ranjith', 'ajay', 'preetham', 'eshwar']
names=input("enter the topic").split(())
enter the topictoken str var comm
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    names=input("enter the topic").split(())
TypeError: must be str or None, not tuple
'ranjith ajay preetham eshwar'.split(' ')
['ranjith', 'ajay', 'preetham', 'eshwar']
names=input("enter the names:").split()
enter the names:ranjith ajay preetham
names
['ranjith', 'ajay', 'preetham']
products=input("enter the products: ").split())
SyntaxError: unmatched ')'
products=input("enter the products: ").split()
enter the products: laptop tv mouse keyboard
products
['laptop', 'tv', 'mouse', 'keyboard']
topics=input("enter the topic").split(())
enter the topictoken str var comm
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    topics=input("enter the topic").split(())
TypeError: must be str or None, not tuple
topics=tuple("enter the topic").split(())
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    topics=tuple("enter the topic").split(())
AttributeError: 'tuple' object has no attribute 'split'
topics=tuple(input("enter the topic").split(())
             topics=input("enter the topic: ").split(())
             
SyntaxError: '(' was never closed
topics=tuple(input("enter the topic: ").split())
             
enter the topic: token str var comm
topics
             
('token', 'str', 'var', 'comm')
op=set(input("enter the operator: ").split())
             
enter the operator: in not is not or not is
op
             
{'is', 'or', 'in', 'not'}
marks=input("enter the marks: ").split())
SyntaxError: unmatched ')'
marks=input("enter the marks: ").split()
enter the marks: 20 12 10 25 50 15
marks
['20', '12', '10', '25', '50', '15']
list(map(int,input("enter the marks: ").split()))
enter the marks: 152
[152]
list(map(int,input("enter the marks: ").split()))
enter the marks: 524 524 256 215 252
[524, 524, 256, 215, 252]
prices=tuple(map(int(,input("Enter the prices: ").split()))
             
SyntaxError: invalid syntax
prices=tuple(map(int(input("Enter the prices: ").split()))
             prices=tuple(map(int(,input("Enter the prices: ").split()))
                          
SyntaxError: invalid syntax. Perhaps you forgot a comma?
prices=tuple(map(int,input("Enter the prices: ").split()))
                          
Enter the prices: 154 458 154 2569 2486 
prices
                          
(154, 458, 154, 2569, 2486)
rating=set(map(int,input("enter the rating: ").split()))
                          
enter the rating: 5 4  4 2 3 5
rating
                          
{2, 3, 4, 5}
per=list(map(float,input("enter the per's:").split()))
                          
enter the per's:52.1 50.1 60.2 75.3
prices=tuple(map(float,input("enter the prices:").split()))
                          
enter the prices:520 600 300 200
prices
                          
(520.0, 600.0, 300.0, 200.0)
a,b=10,20
                          
a
                          
10
b
                          
20
a,b=(10,20)
                          
a
                          
10
b
                          
20
a,b=[10,20]
                          
a
                          
10
b
                          
20
username,passwars=input("enter the usernmae and passward; ").split()
                          
enter the usernmae and passward; codegnan c@123
username
                          
'codegnan'
passward
                          
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    passward
NameError: name 'passward' is not defined. Did you mean: 'passwars'?
passwars
                          
'c@123'
a,b,c,d=list(map(int,input("enter the 4 sides:").split()
  k
                 
SyntaxError: '(' was never closed
a,b,c,d=list(map(int,input("enter the 4 sides:").split()))
                 
enter the 4 sides:2 6 3 4
a
                 
2
b
                 
6
c
                 
3
d
                 
4
price,discount=list(map(float,int().split()))
                 
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    price,discount=list(map(float,int().split()))
AttributeError: 'int' object has no attribute 'split'
>>> price,discount=list(map(float,input().split()))
...                  
2444 50
>>> price
...                  
2444.0
>>> discount
...                  
50.0
>>> a=eval(input())
...                  
3542
>>> a
...                  
3542
>>> a=eval(input())
...                  
5462.1245
>>> a
...                  
5462.1245
>>> 1,2,3,4
...                  
(1, 2, 3, 4)
>>> a
...                  
5462.1245
>>> 1,2,3,4
...                  
(1, 2, 3, 4)
>>> a=eval(input())
...                  
a
>>> a=1,2,3,4
...                  
>>> KeyboardInterrupt
>>> a=eval(input())
...                  
a
>>> b=eval(input())
...                  
1234
>>> b
...                  
1234
