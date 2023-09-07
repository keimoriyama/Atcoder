N = int(input())
S = [input() for _ in range(N)]

ans = 1
for i, s in enumerate(S):
    if s == "OR":
        ans += 2 ** (i + 1)

print(ans)
