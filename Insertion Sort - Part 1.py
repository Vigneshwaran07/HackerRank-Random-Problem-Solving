n = int(input())
a = list(map(int, input().split()))
st = a[-1]
i = n-2
while(st<a[i] and i>=0):
    a[i+1] = a[i]
    print(*a)
    i -= 1
a[i+1] = st
print(*a)
