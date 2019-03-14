for _ in range(int(input())):
    b,w = map(int, input().split())
    bc, wc, z = map(int, input().split())
    if((wc+z)<bc):
        bc = wc+z
    if(bc+z<wc):
        wc = bc+z
    print((b*bc)+(w*wc))
