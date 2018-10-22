import sys
import functools as f
t = int(input().strip())
m = 0
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    for i in range(0,len(num)-k):
        a = list(num[i:i+k])
        a = list(map(int, a))
        ans = f.reduce((lambda x, y: x * y), a) 
        if(m<ans):
            m = ans
    print(m)  
    m = 0
