import itertools
n,d = map(int, input().split())
a = list(map(int, input().split()))
count = 0
for i in itertools.combinations(a, 2):
    if(sum(i)%d == 0):
        count += 1
print(count)
