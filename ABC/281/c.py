N, T = map(int, input().split())
A = list(map(int, input().split()))

A_sum = [A[0]]

for a in A[1:]:
    A_sum.append(A_sum[-1] + a)

s = A_sum[-1]

T = T % s
for i, a in enumerate(A_sum):
    if T > a:
        continue
    if i == 0:
        print(i + 1, T)
        exit()
    else:
        print(i + 1, T - A_sum[i - 1])
        exit()
print(N)
