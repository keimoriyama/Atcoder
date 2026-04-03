N, X = map(int, input().split())
S = list(input())
T = []
for c in S:
    if c == "U" and len(T) > 0 and (T[-1] == "L" or T[-1] == "R"):
        T.pop()
    else:
        T.append(c)

for s in T:
    if s == "L":
        X = 2 * X
    elif s == "R":
        X = 2 * X + 1
    else:
        X = X // 2

print(X)
