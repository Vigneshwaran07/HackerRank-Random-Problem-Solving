n,k = map(int, input().split())
c = []
luck = 0
for i in range(n):
    l, t = map(int, input().split())
    if t == 0:
        luck += l
    else:
        c.append([l,t])
c.sort(key = lambda i:i[0], reverse = True)
try:
    if len(c)==0:
        print(luck)
    else:
        for i in range(k):
            luck += c[i][0]
        if(k==0):
            i = 0
        else:
            i += 1
        while(i<len(c)):
            luck -= c[i][0]
            i += 1
        print(luck)
except:
    print(luck)
