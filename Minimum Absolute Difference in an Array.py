n = int(input())
arr = sorted(list(map(int, input().split())))
m = min(abs(x-y) for x,y in zip(arr,arr[1:]))
print(m)
