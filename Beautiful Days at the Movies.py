s,e,k = map(int, input().split())
count = 0
for i in range(s,e+1):
    if((abs(i-int(str(i)[::-1])))%k == 0):
        count += 1
print(count)        
