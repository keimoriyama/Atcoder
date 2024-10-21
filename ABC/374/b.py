S = list(input())
T = list(input())

for i, (si, ti) in enumerate(zip(S, T)):
    if si == ti:
        continue
    print(i+1)
    exit()
min_N = min(len(S), len(T))
print(0 if len(S) == len(T) else min_N+1)
