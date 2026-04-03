S = input()

N = len(S)
ans = set()
for i in range(N):
    for j in range(i + 1, N + 1):
        ans.add(S[i:j])

print(len(ans))
