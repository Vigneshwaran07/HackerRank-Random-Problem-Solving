from collections import Counter
a = input()
b = input()
uni = list(set(a+b))
acount = Counter(a)
bcount = Counter(b)
delete = 0
for i in uni:
    if acount[i] == bcount[i]:
        continue
    elif acount[i] > bcount[i]:
        delete += acount[i] - bcount[i]
    elif acount[i] < bcount[i]:
        delete += bcount[i] - acount[i]
print(delete)
