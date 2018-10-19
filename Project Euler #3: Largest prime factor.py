import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    maxp = -1
    while n % 2 == 0: 
        maxp = 2
        n = n/2
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxp = i 
            n = n / i
    if n > 2: 
        maxp = n 
      
    print(int(maxp)) 
