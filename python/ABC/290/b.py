N, K = map(int, input().split())
S = input()

n = 0
ans = ""
for s in S:
    if s == "x":
        ans += "x"
    elif s == "o" and n < K:
        ans += "o"
        n += 1
    else:
        ans += "x"

print(ans)
