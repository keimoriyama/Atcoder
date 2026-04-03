N, K = map(int, input().split())
A = list(map(int, input().split()))

offset = 0
if K > N:
    offset = K // N
    K -= N * offset

a_dict = {v: i for i, v in enumerate(A)}

A.sort()
num = [0] * N
i = 0

while K > 0:
    num[a_dict[A[i]]] += 1
    i = (i + 1) % N
    K -= 1

for a in range(N):
    print(num[a] + offset)
