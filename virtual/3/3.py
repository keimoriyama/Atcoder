N = int(input())
A = list(map(int, input().split()))

total = 0
for i in range(N):
    total ^= A[i]

for i in range(N):
    print(total ^ A[i], end=" ")

print()
