S = []
for _ in range(4):
    S.append(input())

check_dict = {"H": 0, "2B": 0, "3B": 0, "HR": 0}

for s in S:
    if s not in check_dict.keys():
        print("No")
        exit()
    check_dict[s] += 1
ans = 0
for v in check_dict.values():
    if v != 1:
        print("No")
        exit()
    else:
        ans += 1

if ans == 4:
    print("Yes")
