from collections import defaultdict

N = int(input())

ac = defaultdict(lambda: 10**10)

for i in range(N):
    a, c = map(int, input().split())
    ac[c] = min(ac[c], a)


ans = 0
for k, v in ac.items():
    ans = max(ans, v)

print(ans)
