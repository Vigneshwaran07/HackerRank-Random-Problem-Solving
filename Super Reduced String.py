a = input()
i = 1
while(i<len(a)):
    if(a[i] == a[i-1]):
        a = a[0:i-1] + a[i+1:]
        i = 0
    i += 1    
print("Empty String" if len(a) == 0 else a)
