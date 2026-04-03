N, Q = map(int, input().split())
S = list(input())

abc = ["A", "B", "C"]
ans = 0
for i in range(N - 2):
    if S[i : i + 3] == abc:
        ans += 1
        
prev_S = S
for i in range(Q):
    X, C = input().split()
    X = int(X) - 1
    for k in range(3):
        idx = X - k
        if 0 <= idx and idx + 2 < N:
            if S[idx : idx + 3] == abc:
                ans -= 1
    S[X] = C
    for k in range(3):
        idx = X - k
        if 0 <= idx and idx + 2 < N:
            if S[idx : idx + 3] == abc:
                ans += 1
    print(ans)
