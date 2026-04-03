N = int(input())
A = list(map(int, input().split()))
X = int(input())
B = [0] * (N)
B[0] = A[0]
for i in range(1, N):
    B[i] = B[i - 1] + A[i]

i = X // B[-1]
X = X - B[-1] * i
ans = i * N
j = 0
while X >= B[j]:
    j += 1


print(ans + j + 1)
