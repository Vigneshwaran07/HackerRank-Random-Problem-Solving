n = int(input())
a = list(map(int, input().split()))
c = 0
num = 0
for i in set(a):
    if a.count(i) > c:
        c = a.count(i)
        num = i
print(num)   
