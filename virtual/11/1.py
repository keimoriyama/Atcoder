N = int(input())
S = sorted([int(input()) for _ in range(N)])

ans = sum(S)
if ans % 10 != 0:
    print(ans)
    exit()

ok = False
n = 0
for i in range(N):
    if S[i] % 10 != 0:
        ok = True
        n = S[i]
        break
if ok:
    print(ans - n)
else:
    print(0)
