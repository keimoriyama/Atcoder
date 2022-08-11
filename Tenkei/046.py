N = int(input())
A = [a % 46 for a in list(map(int, input().split()))]
B = [a % 46 for a in list(map(int, input().split()))]
C = [a % 46 for a in list(map(int, input().split()))]

am = [0] * 46
bm = [0] * 46
cm = [0] * 46

for a, b, c in zip(A, B, C):
    am[a] += 1
    bm[b] += 1
    cm[c] += 1

ans = 0
for i, a in enumerate(am):
    for j, b in enumerate(bm):
        for k, c in enumerate(cm):
            if (i + j + k) % 46 == 0:
                ans += a * b * c
print(ans)
