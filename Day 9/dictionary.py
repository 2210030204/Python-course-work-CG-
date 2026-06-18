Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+9j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+9j): 'complex'}
d[(1,2,3,4)]='tuple'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+9j): 'complex', (1, 2, 3, 4): 'tuple'}
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+9j): 'complex', (1, 2, 3, 4): 'tuple', False: 'bool'}
d=()
d[1]=1
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d[1]=1
TypeError: 'tuple' object does not support item assignment
d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d
{1: 1, 23: 23.4}
d[3]='fvfsvfsv'
d[4]=3+4j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,3}
d[8]=False
d
{1: 1, 23: 23.4, 3: 'fvfsvfsv', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: False}
d={}
d[1]=12
d
{1: 12}
d[1]=14
d
{1: 14}
d={}
d[1]=1
2
2
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8.5:10}
SyntaxError: invalid syntax
d={1:2,2:4,3:6,4:8,5:10}
d[1]
2
d[2]
4
d[3]
6
d[4]
8
d[5]
10
d={'ajay':87,'raju':89,'ram':90,'nuhi':45}
d['ajay']
87
d['raju']
89
d['ram']
90
d.get('ajay')
87
d.items()
dict_items([('ajay', 87), ('raju', 89), ('ram', 90), ('nuhi', 45)])
max(d)
'ram'
ma
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    ma
NameError: name 'ma' is not defined. Did you mean: 'max'?
>>> in(d)
SyntaxError: invalid syntax
>>> min(d)
'ajay'
>>> d['ajay']=100
>>> d
{'ajay': 100, 'raju': 89, 'ram': 90, 'nuhi': 45}
>>> d['ram']=90
>>> d
{'ajay': 100, 'raju': 89, 'ram': 90, 'nuhi': 45}
>>> d['ranjith']=45
>>> d
{'ajay': 100, 'raju': 89, 'ram': 90, 'nuhi': 45, 'ranjith': 45}
>>> d.update({'praneeth':90,'raki':89})
>>> d
{'ajay': 100, 'raju': 89, 'ram': 90, 'nuhi': 45, 'ranjith': 45, 'praneeth': 90, 'raki': 89}
>>> d.popitem()
('raki', 89)
>>> d
{'ajay': 100, 'raju': 89, 'ram': 90, 'nuhi': 45, 'ranjith': 45, 'praneeth': 90}
>>> d.popitem()
('praneeth', 90)
>>> d
{'ajay': 100, 'raju': 89, 'ram': 90, 'nuhi': 45, 'ranjith': 45}
>>> d.pop('subbu')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    d.pop('subbu')
KeyError: 'subbu'
>>> d.pop('ranjith')
45
>>> d
{'ajay': 100, 'raju': 89, 'ram': 90, 'nuhi': 45}
>>> del d['raju']
>>> d
{'ajay': 100, 'ram': 90, 'nuhi': 45}
>>> d.clear()
>>> d
{}
>>> d={'ajay': 100, 'raju': 89, 'ram': 90, 'nuhi': 45, 'ranjith': 45, 'praneeth': 90, 'raki': 89}
>>> d.setdefault('rishi',0)
0
>>> d
{'ajay': 100, 'raju': 89, 'ram': 90, 'nuhi': 45, 'ranjith': 45, 'praneeth': 90, 'raki': 89, 'rishi': 0}
