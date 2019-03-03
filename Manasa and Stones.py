for _ in range(int(input())):
    n = int(input())
    a = int(input())
    b = int(input())
    f = (n-1)*min(a,b)
    s = 0
    print(f,end=" ")
    while(s+f<(n-1)*max(a,b)):
        s+=abs(b-a)
        print(f+s,end=" ")
    print()

