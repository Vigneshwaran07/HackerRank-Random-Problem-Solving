a = []
for _ in range(int(input())):
    a.append(input())
a = sorted(a)
for _ in range(int(input())):
    x = input()
    tot = 0
    for i in x:
        tot += (ord(i))%64
    ind = a.index(x)
    tot = tot*(ind+1)
    print(tot)
