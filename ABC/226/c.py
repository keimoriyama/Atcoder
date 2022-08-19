N = int(input())

l = []
for _ in range(N):
    l.append(list(map(int, input().split())))

f = [0] * N
f[N - 1] = 1
i = N - 1
ans = 0
while i >= 0:
    if f[i]:
        ans += l[i][0]
        for j in range(l[i][1]):
            f[l[i][j + 2] - 1] = 1
    i -= 1
print(ans)
