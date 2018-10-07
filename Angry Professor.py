#https://www.hackerrank.com/challenges/angry-professor/problem

n = int(input())
for i in range(n):
    _,t = map(int, input().split())
    a = list(map(int, input().split()))
    minus = sum(1 for i in a if i < 0)
    zero = a.count(0)
    print("NO" if((minus+zero)>=t) else "YES")
        
