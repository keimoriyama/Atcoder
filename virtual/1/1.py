N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ma = A[0]
c = [A[0] * B[0]]
for i in range(1, N):
    ma = max(ma, A[i])
    c.append(max(c[i - 1], ma * B[i]))

for a in c:
    print(a)
