N = int(input())
a = list(map(int, input().split()))
same = 0
for i in range(N):
    a[i] -= 1

for i, x in enumerate(a):
    if i == x:
        same += 1

ans = same * (same - 1) // 2
for i, j in enumerate(a):
    if i < j and a[j] == i:
        ans += 1

print(ans)