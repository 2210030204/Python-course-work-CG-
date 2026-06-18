s='python'
for i in range(len(s)):
    for j in range(i+1,len(s)):
        print(s[i],s[j],sep='',end=' ')


l=[[1,2,3,],[4,5,6],[7,8,9]]
s= 0
for i in l:
    for j in i:
        s += j
print(s)



    
d={
    '1234':{'pin':'4567','balance':2300},
    '6533':{'pin':'9875','balance':5300},
    '0938':{'pin':'5678','balance':6300},
    '4533':{'pin':'9876','balance':7300}
    }
for i in d:
    print("Account number",i)
    print("pin number:",d[i]['pin'])




