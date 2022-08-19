N = int(input())
S = list(map(int, input().split()))

t = max(S)
ans = [0] * len(S)
menseki = 0
a, b = 1, 1
while menseki <= t:
    while menseki <= t:
        menseki = 4 * a * b + 3 * a + 3 * b
        for i in range(len(S)):
            if S[i] == menseki:
                ans[i] = 1
        a += 1
    a = 1
    b += 1
    menseki = 4 * a * b + 3 * a + 3 * b

ans_1 = 0
for a in ans:
    if a == 0:
        ans_1 += 1
print(ans_1)
