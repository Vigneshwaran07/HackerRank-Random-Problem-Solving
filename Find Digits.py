n = int(input())
a = []
count = 0
for i in range(n):
    a.append(int(input().replace("0","")))
for i in a:
    for j in range(0,len(str(i))):
        if i%int(str(i)[j])==0:
            count += 1
    print(count) 
    count = 0
