L_1, R_1, L_2, R_2 = map(int, input().split())
d = min(R_1, R_2) - max(L_1, L_2)

if d < 0:
    print(0)
else:
    print(d)
