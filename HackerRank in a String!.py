import re
n = int(input())
a=[]
for i in range(n):
    a.append(input())
for i in a:
    print( (re.search('.*'.join("hackerrank"), i) and "YES") or "NO"  )
