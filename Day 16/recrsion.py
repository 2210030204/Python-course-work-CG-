'''def display(s,ind):
    if ind==len(s):
        return
    print(s[:ind+1])
    display(s,ind+1)
display("python",0)'''

'''#OUTPUT:
p
py
pyt
pyth
pytho
python'''

'''def display(s,ind,l):
    if ind==len(s)-l+l:
        return
    print(s[:ind+1])
    display(s,ind+1,l)
display("python programming",0,4)'''


'''#OUTPUT:
p
py
pyt
pyth
pytho
python
python 
python p
python pr
python pro
python prog
python progr
python progra
python program
python programm
python programmi
python programmin
python programming'''



'''def display(l,ind):
    if ind==len(l):
        return 0
    return l[ind]+display(l,ind+1)
l=[1,2,3,4,5,6]
print(display(l,0))'''


'''def display(s,i):
    if i==len(s):
        return 0
    if s[i] in 'aeiouAEIOU':
        return 1+display(s,i+1)
    else:
        return display(s,i+1)
s='python programming'
print(display(s,0))'''


