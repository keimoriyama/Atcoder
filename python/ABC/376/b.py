N, Q = map(int, input().split())
P = [i for i in range(N)]

ans = 0
L, R = 0, 1
for _ in range(Q):
    H, T = input().split()
    T = int(T) - 1
    n_parts = abs(L - R)
    if H == "L":
        exists_R = False
        for i in range(1, N):
            pos = (i + L) % N
            if pos == R:
                exists_R = True
            if P[pos] == T:
                if exists_R:
                    ans += N - i
                else:
                    ans += i
                L = pos
                break
    else:
        exists_L = False
        for i in range(1, N):
            pos = (i + R) % N
            if pos == L:
                exists_L = True
            if P[pos] == T:
                if exists_L:
                    ans += N - i
                else:
                    ans += i
                R = pos
                break
print(ans)
