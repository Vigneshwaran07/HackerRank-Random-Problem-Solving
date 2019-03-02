n,p = map(int, input().split())
a = list(map(int, input().split()))
tot = 0
c=1
for i in a:
    q,r = divmod(i,p)
    if r!=0:
        tot += q+1
    else:
        tot += q
x = [[] for i in range(tot+1)] 
j = 1
for i in a:
    z = iter(list(range(1,i+1)))
    while(1):
        k = next(z,-1)
        
        if(k==-1 and c==0):
            j+=1
            break
        elif(k==-1 and c==1):
            break
        c=0
        x[j].append(k)
        if(len(x[j])==p):
            j += 1
            c=1
            continue
spcl = 0
for ind,i in enumerate (x):
    if(ind in i):
        spcl += 1
print(spcl)
    
