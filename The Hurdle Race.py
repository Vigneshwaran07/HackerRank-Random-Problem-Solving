n, p = map(int,(input().split()))
a = list(map(int, input().split()))
big = max(a)
diff = big - p
if diff > 0:
    print(diff)
else:
    print(0)
