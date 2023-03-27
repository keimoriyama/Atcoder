from collections import defaultdict

S = input()
cnt = [0] * 10

mp = defaultdict(int)
k = "".join(map(str, cnt))
mp[k] += 1

for s in S:
    s = int(s)
    cnt[s] += 1
    cnt[s] %= 2
    k = "".join(map(str, cnt))
    mp[k] += 1

ans = 0
for k, v in mp.items():
    ans += (v * (v - 1)) // 2

print(ans)
