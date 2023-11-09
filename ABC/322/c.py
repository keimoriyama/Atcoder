N, M = map(int, input().split())
A = list(map(int, input().split()))
j = 0
for i in range(1, N + 1):
    diff = A[j] - i
    print(diff)
    if diff == 0:
        j += 1
