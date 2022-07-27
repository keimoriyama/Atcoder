N = int(input())
d = [int(i) for i in input().split()]

ans = 0
for i, x in enumerate(range(len(d))):
    for y in range(i + 1, len(d)):
        ans += d[x] * d[y]

print(ans)
