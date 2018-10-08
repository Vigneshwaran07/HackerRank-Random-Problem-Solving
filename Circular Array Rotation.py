n,k,q = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(q):
    m = int(input())
    print(a[(n+m - (k % n)) % n]) #n-length,k-no.of.rotation,m-index_needed
    
