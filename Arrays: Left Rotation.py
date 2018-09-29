n,d=map(int,input().split(' '))
l=list(map(int,input().split(' ')))
m = [0]*n
for i in range(n):
    new = (i + (n - d)) % n
    m[new] = l[i]  
print(*m) 
