a = input()
b = set(a)
flag = 0
for i in b:
    if a.count(i)%2==0:
        continue
    else:
        flag += 1
print("YES" if(flag==1 or flag==0) else "NO")  
