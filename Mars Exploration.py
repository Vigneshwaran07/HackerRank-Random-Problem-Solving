a = input()
s = "SOS"*(len(a)//3)
count = sum(1 for i in range(0,len(a)) if a[i]!=s[i])
print(count)
