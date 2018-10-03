n = int(input())
count = 0
for i in range(n):
    a = input()
    for k in range(0, len(a)-1):
        if (a[k]==a[k+1]):
            count += 1
    print(count)
    count = 0
