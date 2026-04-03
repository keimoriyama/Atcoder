N = int(input())
A = sorted(list(map(int, input().split())))

for i in range(1, N):
    if A[i - 1] + 1 != A[i]:
        print(A[i - 1] + 1)
