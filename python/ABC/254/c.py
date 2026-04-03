N, K = map(int, input().split())
A = [int(i) for i in input().split()]
B = [[] for _ in range(K)]

for i, x in enumerate(A):
    B[i % K].append(x)
for i in range(K):
    B[i].sort()

SA = []
for i in range(N):
    SA.append(B[i % K][i // K])

if SA == sorted(A):
    print("Yes")
else:
    print("No")
