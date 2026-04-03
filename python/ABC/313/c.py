N = int(input())
A = list(map(int, input().split()))

sum_a = sum(A)
A.sort()

B = [sum_a // N for i in range(N)]

for i in range(0, sum_a % N):
    B[N - i - 1] += 1

ans = 0
for i in range(N):
    ans += abs(A[i] - B[i])

print(ans // 2)
