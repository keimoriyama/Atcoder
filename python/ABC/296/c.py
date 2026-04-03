N, X = map(int, input().split())
A = sorted(list(map(int, input().split())))
S = set(A)

for i in range(N):
    key = A[i] + X
    if key in S:
        print("Yes")
        exit()


print("No")
