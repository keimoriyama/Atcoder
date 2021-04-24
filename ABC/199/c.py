N= int(input())
S = input()
Q = int(input())
S = list(S)
for _ in range(Q):
    tk= input().split()
    T, A, B = int(tk[0]), int(tk[1]),int(tk[2])
    A-=1
    B-=1
    if T == 1:
        tmp = S[A]
        S[A]= S[B]
        S[B] = tmp
    if T == 2:
        tmp = S[:N]
        S[:N] = S[N:]
        S[N:] = tmp

print("".join(S))
