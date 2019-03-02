start = int(input())
end = int(input())
ans = []
if start in range(10):
    ans.append(1)
    start = 9
for i in range(start, end+1):
    if i==1:
        ans.append(1)
    sq = i**2
    x = str(sq)
    r = len(str(i))
    leni = len(str(i))
    lenx = len(x)
    m = int(x[:lenx-leni])
    n = int(x[lenx-leni:])
    if(m+n == i):
        ans.append(i)
if(len(ans)==0):
    print("INVALID RANGE")
else:
    print(*ans)

