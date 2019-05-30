n,t = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
z = 0
for i in a:
    if(i<t):
        t -= i
        z += 1
print(z)
