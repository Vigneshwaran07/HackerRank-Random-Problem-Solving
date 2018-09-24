items,noteat = map(int,input().split())
a = list(map(int, input().split()))
bill = int(input())
del(a[noteat])
if sum(a)//2 == bill:
    print("Bon Appetit")
else:
    print(bill - sum(a)//2)
