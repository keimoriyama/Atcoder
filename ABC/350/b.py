N, Q = map(int, input().split())
T = list(map(int, input().split()))
ha = [True for _ in range(N)]
for t in T:
    t -= 1
    ha[t] = not ha[t]
print(sum(ha))
