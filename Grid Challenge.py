for _ in range(int(input())):
    n = int(input())
    flag = 0
    arr = []
    for i in range(n):
        arr.append(sorted(input()))
    for i in zip(*arr):
        if (list(i) != sorted(i)):
            flag = 1
            break
    print("YES" if flag==0 else "NO")
