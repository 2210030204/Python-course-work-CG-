for row in range(5):
    for col in range(5):
        print(col,end=' ')
    print()


n=int(input("Enter the size"))
for row in range(n):
    for col in range(n):
        print('*',end=' ')
    print()


n=int(input())
for row in range(n):
    for col in range(n):
        print(col%2,end='')
    print()
        
n=int(input())
for row in range(n):
    for col in range(row+1):
        print('*',end='')
    print()


n=int(input())
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    print()


n=int(input())
for i in range(n):
    for sp in range(n-1-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()


n=int(input())
for row in range(n):
    for sp in range(row):
        print(' ',end=' ')
    for j in range(n-row):
        print('*',end=' ')
    print()


n=int(input())
for i in range(n):
    for j in range(n):
        print((i + j) % 2, end=" ")
    print()

        


n = 5
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
