input()
a = input()
n = int(input())
for i in a:
    num = ord(i)
    if 97 <= num <= 122:
        print (chr(((num-97+n)%26)+97),end="")
    elif 65 <= num <= 90:
        print (chr(((num-65+n)%26)+65),end="")
    else: print(i,end='')
