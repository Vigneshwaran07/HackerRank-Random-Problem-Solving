s = input()
t = input()
k = int(input())
low = min(len(s), len(t))
for i in range(len(t)):
    if s[:i] != t[:i]:
        low = i-1
        break

diff = len(s)-low + len(t)-low
print('Yes' if (diff <= k and diff%2 == k%2) or len(s) + len(t) < k else 'No')
