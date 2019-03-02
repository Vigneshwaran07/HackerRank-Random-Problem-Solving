for _ in range(int(input())):
    a = input()
    b = input()
    if(any(i in b for i in a )):
        print("YES")
    else:
        print("NO")
