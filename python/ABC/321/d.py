import bisect

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))

B_sum = [0]
for b in B:
    B_sum.append(B_sum[-1] + b)

ans = 0
for a in A:
    i = bisect.bisect(B, P - a)
    ans += a * i
    ans += (M - i) * P
    ans += B_sum[i]

print(ans)
