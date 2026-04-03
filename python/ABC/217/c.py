N = int(input())
p = [0] + list(map(int, input().split()))
q = [-1] * (N + 1)
for i in range(1, N + 1):
    q[p[i]] = i

print(*q[1:])
