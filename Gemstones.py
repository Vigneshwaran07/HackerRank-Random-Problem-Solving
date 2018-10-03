n = int(input())
a = []
for i in range(n):
    a.append(input())
k = a[0]    
for i in a:
    k = set(k).intersection(i)
print(len(k))    
