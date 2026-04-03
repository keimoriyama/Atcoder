N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort()

F_sum = [F[0]]
for f in F[1:]:
    F_sum.append(F_sum[-1] + f)


max_k = (N + D - 1) // D
ans = P * max_k
for k in range(max_k):
    ans = min(ans, k * P + F_sum[N - k * D - 1])

print(ans)
