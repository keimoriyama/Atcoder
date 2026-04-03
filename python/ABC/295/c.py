from collections import Counter

N = int(input())
A = list(map(int, input().split()))

A = Counter(A)

ans = 0
for k, v in A.items():
    ans += v // 2

print(ans)
