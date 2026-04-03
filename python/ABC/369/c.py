from math import comb
N = int(input())
A = list(map(int, input().split()))

A_diff = []
for i in range(1, N):
    A_diff.append(A[i] - A[i - 1])
    
ans = 2 * N - 1

j = 0
tmp = 1
for i in range(1, len(A_diff)):
    if A_diff[j] == A_diff[i]:
        tmp += 1
    else:
        ans += comb(tmp, 2)
        j = i
        tmp = 1
if tmp > 1:
    ans += comb(tmp, 2)
print(ans)
