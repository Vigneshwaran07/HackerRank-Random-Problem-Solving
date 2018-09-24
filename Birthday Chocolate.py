n = int(input())
a = list(map(int, input().split()))
d,m = map(int, input().split())
ways = 0
for i in range(0, n):
    if sum(a[i:i+m]) == d:
        ways += 1
print(ways) 
