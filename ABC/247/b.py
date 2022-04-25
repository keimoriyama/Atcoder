N = int(input())
S, T = [], []
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)
for i in range(N):
    can = False
    for S1 in [S[i], T[i]]:
        s_ok = True
        for j in range(N):
            if i != j:
                if S1 == S[j] or S1 == T[j]:
                    s_ok = False
        if s_ok == True:
            can = True
    if can == False:
        print("No")
        exit()
print("Yes")