X = input()
N = int(input())
S = []
s_dict = {v: i for i, v in enumerate(X)}
for _ in range(N):
    S.append(input())

s_num = {}
for i, s in enumerate(S):
    num = []
    for s_c in s:
        num.append(s_dict[s_c])
    s_num[i] = num

s_num = sorted(s_num, key=lambda x: s_num[x])

for s in s_num:
    print(S[s])
