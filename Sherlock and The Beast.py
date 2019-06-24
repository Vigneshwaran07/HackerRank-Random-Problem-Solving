for _ in range(int(input())):
    a = int(input())
    b = a
    while(b%3!=0):
        b -= 5
    if(b<0):
        print(-1)
    else:
        print(b*'5'+(a-b)*'3')
