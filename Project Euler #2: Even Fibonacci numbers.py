import sys
def efib(limit):
    a, b = 0, 1
    while a < int(limit):
        if not a % 2:         
            yield a
        a, b = b, a + b

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum(efib(n)))
