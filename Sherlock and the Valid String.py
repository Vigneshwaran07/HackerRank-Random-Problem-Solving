from collections import Counter
a = input()
c = dict(Counter(a))
l = list(c.values())
if(max(l)-min(l)==0):
    print("YES")
elif(l.count(max(l))==1 and max(l)-min(l) == 1):
    print("YES")
elif(l.count(min(l))==1):
    l.remove(min(l))
    if(max(l)-min(l)==0):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
