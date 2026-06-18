n= int(input("enter the size:"))
m=n//2
for i in range(n):
    if i<m:
        print("*" *(i+1),end=' ')
    else:
        print("*" *(n-i),end=' ')
    print()


'''OUTPUT:
enter the size:10
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''


n=int(input("enter the size:"))
m=n//2
for i in range(n):
    if i<=m:
        print('  '*(m-i),end=' ')
        print('* '*(i+1),end=' ')
    else:
        print('  '*(i-m),end=' ')
        print('* '*(n-i),end=" ")
    print()

'''OUTPUT:
enter the size:15
               *  
             * *  
           * * *  
         * * * *  
       * * * * *  
     * * * * * *  
   * * * * * * *  
 * * * * * * * *  
   * * * * * * *  
     * * * * * *  
       * * * * *  
         * * * *  
           * * *  
             * *  
               *  
'''

n=int(input("enter the size:"))
m=n//2
for i in range(n):
    if i<m:
        print('  '*(m-i),end=' ')
        print(' *  '*(i+1),end=' ')
    else:
        print('  '*(i-m),end=' ')
        print(' *  '*(n-i),end=" ")
    print()

'''OUTPUT:
    enter the size:15
                *   
              *   *   
            *   *   *   
          *   *   *   *   
        *   *   *   *   *   
      *   *   *   *   *   *   
    *   *   *   *   *   *   *   
  *   *   *   *   *   *   *   *   
    *   *   *   *   *   *   *   
      *   *   *   *   *   *   
        *   *   *   *   *   
          *   *   *   *   
            *   *   *   
              *   *
                *
                '''

n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''OUTPUT:
Enter the size:9
* * * * * * * * * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
* * * * * * * * *
'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or i==n-1 or j==n//2 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''OUTPUT:
Enter the size:9
* * * * * * * * * 
*       *       * 
*       *       * 
*       *       * 
* * * * * * * * * 
*       *       * 
*       *       * 
*       *       * 
* * * * * * * * *
'''


n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0  or i==n-1 or j==i or j==0 or j==n-1 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''OUTPUT:
Enter the size:11
* * * * * * * * * * * 
* *               * * 
*   *           *   * 
*     *       *     * 
*       *   *       * 
*         *         * 
*       *   *       * 
*     *       *     * 
*   *           *   * 
* *               * * 
* * * * * * * * * * *
'''

n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''   oUTPUT:
Enter the size:11
* * * * * * * * * * * 
*                   * 
*                   * 
*                   * 
*                   * 
* * * * * * * * * * * 
*                   * 
*                   * 
*                   * 
*                   * 
*                   *'''
                      



n = int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if j == 0 or ((i == 0 or i == n//2 or i == n-1) and j < n-1) or (j == n-1 and i not in [0, n//2, n-1]):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''Output
Enter the size:11
* * * * * * * * * *   
*                   * 
*                   * 
*                   * 
*                   * 
* * * * * * * * * *   
*                   * 
*                   * 
*                   * 
*                   * 
* * * * * * * * * *   '''

n = int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''Enter the size:11
* * * * * * * * * * * 
*                     
*                     
*                     
*                     
*                     
*                     
*                     
*                     
*                     
* * * * * * * * * * * '''
n = int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

   ''' Enter the size:11
* * * * * * * * * * * 
*                   * 
*                   * 
*                   * 
*                   * 
*                   * 
*                   * 
*                   * 
*                   * 
*                   * 
* * * * * * * * * * * '''

n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==m:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

'''Enter the size:11
* * * * * * * * * * * 
*                     
*                     
*                     
*                     
* * * * * * * * * * * 
*                     
*                     
*                     
*                     
* * * * * * * * * * * '''
n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==m:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

'''Enter the size:11
* * * * * * * * * * * 
*                     
*                     
*                     
*                     
* * * * * * * * * * * 
*                     
*                     
*                     
*                     
*       '''



