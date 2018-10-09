import math as m
for _ in range(int(input())):
    a, b = map(int, input().split())
    print((m.floor(m.sqrt(b))) - (m.ceil(m.sqrt(a)))+1)
