N = int(input())
S = [int(s) for s in input()]
W = list(map(int, input().split()))
sort_list = zip(W, S)
sort_list = sorted(sort_list)
W, S = zip(*sort_list)

ans = 0
for s in S:
    if s == 1:
        ans += 1
x = ans

for i in range(N):
    if S[i] == 1:
        x -= 1
    else:
        x += 1
    if i < (N - 1):
        if W[i] != W[i + 1]:
            ans = max(ans, x)
    else:
        ans = max(ans, x)

print(ans)
