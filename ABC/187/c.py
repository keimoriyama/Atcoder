def check_str(trg):
    if trg[0] == "!":
        return trg.replace("!", "")
    else:
        return "!" + trg

N = int(input())

S_list = []

flag = False

for i in range(N):
    S_list.append(input().replace("\r", ""))

for S in S_list:
    S = check_str(S)
    for trg_S in S_list:
        if S == trg_S and not flag:
            if S[0] == "!":
                S.replace("!", "")
            print(S)
            flag = True
            break

if not flag:
    print("satisfiable")