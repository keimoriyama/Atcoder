S = input()
K = int(input())

c = [0] * (len(S) + 1)
for i in range(len(S)):
    if S[i] == ".":
        c[i + 1] = c[i] + 1
    else:
        c[i + 1] = c[i]

ans, r = 0, 0
for i in range(len(S)):
    while r <= len(S) - 1 and c[r + 1] - c[i] <= K:
        r += 1
    ans = max(ans, r - i)
print(ans)
