_ = int(input())
a = list(map(int, input().split()))
for i in range(1,len(a)):
    s = a[i]
    j = i-1
    while(j>=0 and s<a[j]):
        a[j+1] = a[j]
        j -= 1
    a[j+1] = s
    print(*a)
