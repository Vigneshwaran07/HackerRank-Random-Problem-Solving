for _ in range(int(input())):
    s = input()
    c = 0
    if(len(s)%2!=0):
        print(-1)
    else:
        s1 = s[:(len(s)//2)]
        s2 = s[len(s)//2:]

        if(s1==s2):
            print(0)
        else:
            for i in s1:
                f = s2.find(i)
                if(f!=-1):
                    s2 = s2.replace(i,'',1)
                    s1 = s1.replace(i,'',1)
        print(min(len(s1),len(s2)))
