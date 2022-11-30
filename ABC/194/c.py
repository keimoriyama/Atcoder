N = int(input())
a = list(map(int, input().split()))

cnt = {i: 0 for i in range(-200, 201)}
for a_i in a:
    cnt[a_i] += 1

ans = 0
for i, vi in zip(cnt.keys(), cnt.values()):
    for j, vj in zip(cnt.keys(), cnt.values()):
        if i > j:
            continue
        ans += vi * vj * abs(i - j) ** 2

print(ans)
