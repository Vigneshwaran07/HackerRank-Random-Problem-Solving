n = int(input())
a =[list(input()) for i in range(n)]
#a=[['1112'],['1912'],['1892'],['1234']]
for i in range(1,n-1):
    for j in range(1,n-1):
        if(a[i][j]>max(a[i][j-1],a[i][j+1],a[i+1][j],a[i-1][j])):
            a[i][j]='X'
            
for i in a:
    print(''.join(i))    
