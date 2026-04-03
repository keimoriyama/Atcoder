# TLEした！！！

N = int(input())
A = input().split()

A = list(map(int, A))
ans = 0

for i in range(N-1):
    for j in range(i+1, N):
        ans += abs(A[i] - A[j])

print(ans)
