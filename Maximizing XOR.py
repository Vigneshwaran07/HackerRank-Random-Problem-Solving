a = int(input())
b = int(input())
arr = list(range(a,b+1))
l = []
from itertools import combinations
for i in combinations(arr, 2):
    x,y = i
    l.append(x^y)
print(max(l))
