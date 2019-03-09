from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
brr = list(map(int, input().split()))
a = Counter(arr)
b = Counter(brr)
print(*sorted((b - a).keys()))
