s1 = input()
s2 = input()
for i in s1:
    f = s2.find(i)
    if(f!=-1):
        s2 = s2.replace(i,'',1)
        s1 = s1.replace(i,'',1)
print(len(s1+s2))
