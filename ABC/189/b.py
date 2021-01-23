N, X = map(int, input().split(' '))

V, P = [], []

alchol = 0
flag = False

for i in range(N):
    v, p = input().split(' ')
    V.append(int(v))
    P.append(int(p))

for i in range(N):
    alchol += V[i] * (P[i]/100)
    # print(alchol)
    if alchol > X and not flag:
        print(alchol)
        flag = True
        print(i+1)

if not flag:
    print('-1')


