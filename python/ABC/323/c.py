N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

Ai = [(a, i) for i, a in enumerate(A)]
score = []

for i in range(N):
    si = S[i]
    scorei = i + 1
    for j in range(M):
        if si[j] == "o":
            scorei += A[j]
    score.append(scorei)

boarder = max(score)
# print(score)
Ai_sort = sorted(Ai, reverse=True)
# print(Ai_sort)
for i in range(N):
    if score[i] == boarder:
        print(0)
        continue
    n = 0
    for ai in Ai_sort:
        idx = ai[1]
        v = ai[0]
        if S[i][idx] == "o":
            continue
        if score[i] + v >= boarder:
            print(n + 1)
            break
        else:
            n += 1
            score[i] += v
