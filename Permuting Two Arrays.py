for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))[::-1]
    f = 0
    if(any(a[i]+b[i] < k for i in range(len(a)))):
        print("NO")
    else:
        print("YES")
