Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord('a)
    
SyntaxError: unterminated string literal (detected at line 1)
ord('a')
    
97
ord('A')
    
65
chr(120)
    
'x'
chr(90)
    
'Z'
chr(30)
    
'\x1e'
chr(35)
    
'#'
chr(37)
    
'%'
chr(65)
    
'A'
s='python Programming'
    
s.upper()
    
'PYTHON PROGRAMMING'
s.lower()
    
'python programming'
s.capitalize()
    
'Python programming'
s.title()
    
'Python Programming'
s.swapcase()
    
'PYTHON pROGRAMMING'
"STRABEMALAGAAngstromCafe".casefold()
    
'strabemalagaangstromcafe'
 s
    
SyntaxError: unexpected indent
s
    
'python Programming'
len(s)
    
18
s.center(28'-')
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.center(28,'-')
    
'-----python Programming-----'
s.ljust(28'-')
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.ljust(28,'-')
    
'python Programming----------'
s.rjust(28,'-')
    
'----------python Programming'
'123'.zfill(5)
    
'00123'
'123'.zfill(10)
    
'0000000123'
'123'.zfill(3)
    
'123'
'123'.zfill(2)
    
'123'
s
    
'python Programming'
s.find('o')
    
4
s.find('g')
    
10
s.rfind('g')
    
17
s.rfind('z')
    
-1
s.index('o')
    
4
s.rindex('o')
    
9
s.count('y')
    
1
s.count('n')
    
2
s.count('g')
    
2
s
    
'python Programming'
s.replace('python','java')
    
'java Programming'
s.maketrans('python','123456')
    
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('python','123456'))
    
'123456 Pr5grammi6g'
s='java,python,javascript,c,c++'
    
s.split(',')
    
['java', 'python', 'javascript', 'c', 'c++']
>>> s.split(',',2)
...     
['java', 'python', 'javascript,c,c++']
>>> s.rsplit(',',2)
...     
['java,python,javascript', 'c', 'c++']
>>> g='sdfgh'
...     
>>> g='gfddhhfadfhag'
...     
>>> g='nhjgf'
...     
>>> g='jfgjjgfj'
...     
>>> g
...     
'jfgjjgfj'
>>> 
>>> 
>>> s.splitlines()
...     
['java,python,javascript,c,c++']
>>> g.splitlines()
...     
['jfgjjgfj']
>>> l='java,python,javascript,c,c++'
...     
>>> ''.join(l)
...     
'java,python,javascript,c,c++'
>>> '-'.join(l)
...     
'j-a-v-a-,-p-y-t-h-o-n-,-j-a-v-a-s-c-r-i-p-t-,-c-,-c-+-+'
>>> '@'.join(l)
...     
'j@a@v@a@,@p@y@t@h@o@n@,@j@a@v@a@s@c@r@i@p@t@,@c@,@c@+@+'
>>> s
...     
'java,python,javascript,c,c++'
>>> s.partition(',')
...     
('java', ',', 'python,javascript,c,c++')
>>> s.rpartition(',')
...     
('java,python,javascript,c', ',', 'c++')
