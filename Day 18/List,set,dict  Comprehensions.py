res1=[i for i in range(1,11)]
print(res1)

'''OUTPUT:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''



res2=[i for i in range(3,31,3)]
print(res2)

'''OUTPUT:
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]'''


res3=[i for i in range(2,51,2)]
print(res3)

'''#OUTPUT:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]'''


a='Python Programming'
l1=[ i for i in a if i in 'aeiouAEIOU']
print(l1)


'''#OUTPUT:
['o', 'o', 'a', 'i']'''



a=[1,2,4,5,6,8,9,11,2,32,45,65,67,80]
l2=[i if i%2==0 else 0 for i in a]
print(l2)


'''#OUTPUT:
[0, 2, 4, 0, 6, 8, 0, 0, 2, 32, 0, 0, 0, 80]'''




'''l=[int(input(f"ENter the number -{i+1}: ")) for i in range(10)]
print(l)'''

'''#OUTPUT:
ENter the number -1: 1
ENter the number -2: 2
ENter the number -3: 34
ENter the number -4: 54
ENter the number -5: 67
ENter the number -6: 87
ENter the number -7: 98
ENter the number -8: 90
ENter the number -9: 75
ENter the number -10: 45
[1, 2, 34, 54, 67, 87, 98, 90, 75, 45]'''

ll=[j for i in range(3) for j in range(1,4)]
print(ll)

'''#OUTPUT:
1, 2, 3, 1, 2, 3, 1, 2, 3]'''


lst=[[j for j in range(1,4)] for i in range(3)]
print(lst)


'''#OUTPUT:
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]'''

s1={i for i in range(1,11)}
print(s1)

'''#OUTPUT:
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}'''


d={}
for i in range(1,11):
    d[i]=i*i
print(d)


d={i:i*i for i in range(1,11)}
print(d)

'''#OUTPUT:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}'''


t={input("Enter the name:"):int(input("Enter the marks:")) for i in range(5)}
print(t)

'''#OUTPUT:
Enter the name:Ajay
Enter the marks:98
Enter the name:ram
Enter the marks:76
Enter the name:sai
Enter the marks:46
Enter the name:deeru
Enter the marks:78
Enter the name:reddy
Enter the marks:69
{'Ajay': 98, 'ram': 76, 'sai': 46, 'deeru': 78, 'reddy': 69}'''



