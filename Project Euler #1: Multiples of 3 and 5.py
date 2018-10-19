import sys
def factor(k, n):
    m = (k-1)//n
    return n*m*(m+1) //2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(factor(n,3)+ factor(n,5)-factor(n,15))
    
   
