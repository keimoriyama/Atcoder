N = int(input())
S = input()
Q = int(input())
S = list(S)
turn = False
for _ in range(Q):
    tk = input().split()
    T, A, B = int(tk[0]), int(tk[1]), int(tk[2])
    A -= 1
    B -= 1
    if T == 1:
        if turn:
            if A < N:
                A = N + A
            else:
                A = A - N
            if B < N:
                B = N + B
            else:
                B = B - N
        S[A], S[B] = S[B], S[A]
    if T == 2:
        turn = not turn
if turn:
    tmp = S[:N]
    S[:N] = S[N:]
    S[N:] = tmp

print("".join(S))
