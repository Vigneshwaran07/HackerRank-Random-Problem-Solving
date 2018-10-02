b, n, m = map(int, input().split())
k = list(map(int, input().split()))
u = list(map(int, input().split()))
k = sorted(k, reverse=True)
u = sorted(u)
maxi = -1
for i in k:
    for j in u:
        if i+j > b:
            break
        if i+j > maxi:
            maxi = i+j
print(maxi) 
