import math as m
for _ in range(int(input())):
    a = m.factorial(int(input()))
    s = sum(list(map(int, list(str(a)))))
    print(s)
