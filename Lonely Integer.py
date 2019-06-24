from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
count = Counter(arr)
for i in count:
    if count[i]==1:
        print(i)
        break
