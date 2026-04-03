from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]


def calc_diff(s1, s2):
    d = 0
    for s11, s21 in zip(s1, s2):
        if s11 == s21:
            continue
        d += 1
    return d


for T in permutations(S):
    ok = True
    for i in range(N - 1):
        d = calc_diff(T[i], T[i + 1])
        if d != 1:
            ok = False
    if ok:
        print("Yes")
        exit()


print("No")
