n,k,q = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(k):
    a = [a[-1]]+a[0:-1]
for _ in range(q):
    print(a[int(input())])
    
