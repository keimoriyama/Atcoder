N, M = map(int, input().split())
S = input().split()
T = input().split()
i = 0
t = T[i]
for s in S:
    if s == t:
        print("Yes")
        i += 1
        if i == len(T):
            break
        t = T[i]
    else:
        print("No")
