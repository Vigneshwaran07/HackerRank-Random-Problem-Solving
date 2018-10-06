input()
a = list(map(int, input().split()))
while(1):
    m = min(a)
    if len(a) == 0:
        break
    else:
        print(len(a))
    a = list(filter(lambda x: x != m, a)) 
    for i in range(0, len(a)):
        a[i] = a[i] - m
    a =  list(filter(lambda x: x > 0, a))    
