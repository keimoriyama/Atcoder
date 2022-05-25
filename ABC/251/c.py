N = int(input())
S, T = [], []
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))

s = set()
best_score = -1
index = -1
for i in range(N):
    if S[i] in s:
        continue
    s.add(S[i])
    if best_score < T[i]:
        best_score = T[i]
        index = i + 1

print(index)
