S = list(input())
T = list(input())

X = []
wrote = [False] * len(T)
while S != T:
    x = []
    for  i in range(len(T)):
        if S[i] != T[i]:
            tmp = S.copy()
            tmp[i] = T[i]
            x.append("".join(tmp))
    x = sorted(x)
    X.append(x[0])
    S = list(x[0])
            

print(len(X))
for xi in X:
    print(xi)
