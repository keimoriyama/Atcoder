N = int(input())
A = list(map(int, input().split()))

d = {i: 0 for i in range(-200, 201)}

for a in A:
    d[a] += 1

ans = 0
for i in range(-200, 201):
    for j in range(-200, 201):
        if i > j:
            continue
        ans += d[i] * d[j] * abs(i - j) ** 2

print(ans)
