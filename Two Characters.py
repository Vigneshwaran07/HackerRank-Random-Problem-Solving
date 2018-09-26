import itertools
from collections import Counter
n =  int(input())
a = input()
b = set(a)
r = len(b)-2
count = 0
high = 0
if len(b) > 1:
    for i in itertools.combinations(b,r):
        temp = a
        for j in i:
            temp = temp.replace(j,"")
        count = len(temp)
        k = ([[k, len(list(g))] for k, g in itertools.groupby(temp)])
        if(any((k[i][1]>=2 for i in range(0,len(k))))):
            pass
        elif(count > high):
            high = count
    print(high)
else:
    print(high)
