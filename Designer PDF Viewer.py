a = list(map(int, input().split()))
s = input()
value = max(list(a[ord(i)%97] for i in s))
print(value *len(s))
