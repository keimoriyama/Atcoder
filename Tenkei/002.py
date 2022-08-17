def check(S):
    d = 0
    for s in S:
        if s == "(":
            d += 1
        if s == ")":
            d -= 1
        if d < 0:
            return False
    if d == 0:
        return True
    else:
        return False


N = int(input())

i = 0
while i < 1 << N:
    S = ""
    j = N - 1
    while j >= 0:
        if i & (1 << j):
            S += ")"
        else:
            S += "("
        j -= 1
    if check(S):
        print(S)
    i += 1
