from collections import defaultdict

S = input()

X = []
Y = defaultdict(int)
n = set()
for s in S:
    if s == "(":
        X.append(n)
        n = set()
    elif s == ")":
        for k in list(n):
            Y[k] = 0
        n = X.pop(-1)
    else:
        n.add(s)
        if Y[s] == 1:
            print("No")
            exit()
        Y[s] = 1
print("Yes")
