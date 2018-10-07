input()
a = input()
count = 0
ans = 0
for i in a:
    if (i == "U"):
        count += 1
    if (i == "D"):
        count -= 1
    if (count == 0 and i == 'U'):
        ans += 1
print(ans)        
        
