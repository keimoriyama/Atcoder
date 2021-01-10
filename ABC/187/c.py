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
    if S in S_list:
        S.replace("!", "")
        print(S)
        flag = True
        break

if not flag:
    print("satisfiable")