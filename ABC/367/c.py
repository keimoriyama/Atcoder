N, K = map(int, input().split())
R = list(map(int, input().split()))

num = [1] * N
head = 0
ans = []
while R[N - 1] >= num[N - 1]:
    if sum(num) % K == 0:
        ans.append(int("".join([str(n) for n in num])))
    num[0] += 1
    i = 0
    while num[i] > R[i] and i + 1 < N:
        num[i] = 1
        num[i + 1] += 1
        i += 1

ans = sorted(ans)

for a in ans:
    print(" ".join(list(str(a))))
