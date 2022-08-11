N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 1
for d in A:
    t = sum(d)
    ans *= t
print(ans % 1000000007)
