N, A, B = map(int, input().split())
S = input()

S += S

ans = 1 << 60
for i in range(N):
    tmp = A * i
    for j in range(N // 2):
        if S[i + j] != S[i + N - 1 - j]:
            tmp += B
    ans = min(ans, tmp)
print(ans)
