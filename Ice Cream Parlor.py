import itertools as it
for _ in range(int(input())):
    cost = int(input())
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(0,n):
        for j in range(i+1,n):
            if(a[i]+a[j]==cost):
                print(i+1,j+1)
                
