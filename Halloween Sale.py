
p, d, m, s = map(int, input().split())
i = 0
cost = p
while s-cost>=0:
    i+=1
    s-=cost
    cost = max(cost-d,m)
print(i)   
