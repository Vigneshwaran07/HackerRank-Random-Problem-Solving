n = int(input())
p = list(map(int, input().split()))
q = [0 for i in range(n)]
for i in p:
    q[p[p[i-1]-1]-1] = i
print(*q,sep="\n")
