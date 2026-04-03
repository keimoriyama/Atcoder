N, M, D = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)

ans = -1
i, j = 0, 0

while True:
    if i >= N or j >= M:
        break
    if abs(A[i] - B[j]) <= D:
        ans = A[i] + B[j]
        print(ans)
        exit()
    else:
        if A[i] > B[j]:
            i += 1
        else:
            j += 1

print(-1)
