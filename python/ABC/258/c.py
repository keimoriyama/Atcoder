N, Q = map(int, input().split())
S = input()
shift = 0
for q in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        shift = (shift + x) % N 
    elif t == 2:
        x -= 1
        idx = x - shift
        if idx < 0:
            idx = N + idx
        print(S[idx])
