Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=' hello,  wprld    '
s
' hello,  wprld    '
s.strip()
'hello,  wprld'
s.lstrip()
'hello,  wprld    '
s.rstrip()
' hello,  wprld'
>>> s='string.py'
>>> s
'string.py'
>>> s.startswith()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.startswith()
TypeError: startswith expected at least 1 argument, got 0
>>> s.startswith('str')
True
>>> s.startswith('gfh')
False
>>> s.endswith('py')
True
>>> s.endswith('ert')
False
>>> 'hvvhfmvmvkhvsvv'.isalpha()
True
>>> 'bscdvvgkdvwhvwvkvkw'.isalpha()
True
>>> 'wddw3443%%%%'.isalpha()
False
>>> '123456'.isalnum()
True
>>> 'dkhdhfadf'.isalnum()
True
>>> 'sbfsf%$##'.isalnum()
False
>>> 'dsgfgffsffbfs'.islower()
True
>>> 'GBHHHKHKKJKH'.isupper()
True
>>> ' '.isspace()
True
>>> 'hello       ',isspace()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    'hello       ',isspace()
NameError: name 'isspace' is not defined
>>> 'hello       '.isspace()
False
>>> 'Py arg am'.istitle()
False
>>> 'py_python'.isidentifier()
True
