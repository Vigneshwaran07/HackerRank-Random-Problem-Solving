n = int(input())
for i in range(n):
    a = int(input())
    k = a//2
    m = 1 if a%2==0 else 2
    print(2**(k+m)-m)
        
