n = int(input())
for i in range(n):
    a=input()
    aski = [ord(ch) for ch in a]
    askir = [ord(ch) for ch in a[::-1]]
    saski = [abs(aski[i] - aski[i+1]) for i in range(len(a)-1)]
    saskir = [abs(askir[i] - askir[i+1]) for i in range(len(a)-1)]
    if(saski == saskir):
        print("Funny")
    else:
        print("Not Funny")
