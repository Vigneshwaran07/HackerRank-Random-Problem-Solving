_ = int(input())
a = list(map(int, input().split()))
high = []
for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        if(a[i] == a[j]):
            high.append(abs(i-j))
            break
print(-1 if len(high)==0 else min(high))      
