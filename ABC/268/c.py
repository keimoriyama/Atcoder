N = int(input())
p = list(map(int, input().split()))

c = [0] * (N + 1)

for i in range(N):
    for j in range(3):
        c[(p[i] - 1 - i + N + j) % N] += 1
    print(c)

ans = max(c)
print(ans)
