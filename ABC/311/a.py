N = int(input())
S = input()

d = {"A": 0, "B": 0, "C": 0}

for i, s in enumerate(S):
    d[s] += 1
    ok = True
    for v in d.values():
        if v == 0:
            ok = False
    if ok:
        print(i + 1)
        exit()
