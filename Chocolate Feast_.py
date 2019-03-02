for _ in range(int(input())):
    n,c,m = map(int, input().split())
    wrap = 0
    eat = n//c
    wrap = eat
    while(wrap >= m):
        cureat = wrap//m
        eat += cureat
        wrap = wrap-(m*(cureat))
        wrap += cureat
    print(eat)
