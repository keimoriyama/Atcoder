N, M = map(int, input().split())
S = input()
T = input()

ans = 0
f = True
res = []
for i in range(min(len(S), len(T))):
    if S[i] != T[i]:
        f = False
res.append(f)

f = True
for i in range(min(len(S), len(T))):
    if S[N - i - 1] != T[M - i - 1]:
        f = False
res.append(f)


if res[0] and res[1]:
    print(0)
elif not res[0] and res[1]:
    print(2)
elif res[0] and not res[1]:
    print(1)
else:
    print(3)
