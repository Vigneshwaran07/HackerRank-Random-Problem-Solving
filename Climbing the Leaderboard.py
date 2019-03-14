n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
leaderboard = sorted(set(a), reverse = True)
l = len(leaderboard)
for i in b:
    while (l > 0) and (i >= leaderboard[l-1]):
        l -= 1
    print (l+1)
