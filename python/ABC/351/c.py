N = int(input())
A = list(map(int, input().split()))

S = []
for ai in A:
    S.append(ai)
    while len(S) >= 2:
        if S[-1] == S[-2]:
            ai = S.pop()
            aj = S.pop()
            S.append(ai + 1)
        else:
            break


print(len(S))
