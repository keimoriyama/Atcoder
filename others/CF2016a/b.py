N = int(input())
A = list(map(int, input().split()))

s = set()

ans = 0
for i in range(N):
    if i in s:
        continue
    a_i = A[i] - 1
    a_j = A[a_i] - 1
    if i == a_j:
        ans += 1
        s.add(a_i)

    s.add(i)


print(ans)
