n = input()
a = list(map(int, input().split()))
min_count = max_count = 0
high = low = a[0]
for i in range(0, len(a)):
    if a[i] < low:
        low = a[i]
        min_count += 1
    if a[i]> high:
        high = a[i]
        max_count += 1
print(max_count,min_count)        
