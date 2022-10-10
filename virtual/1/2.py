N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ans = 10**10

i, j = 0, 0

while i < N and j < M:
    ans = min(abs(A[i] - B[j]), ans)
    if A[i] < B[j]:
        i += 1
    else:
        j += 1

print(ans)
