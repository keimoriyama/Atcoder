N = int(input())
S = []
for _ in range(N):
    S.append(input())

first = set(["H", "D", "C", "S"])
second = set(["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"])

if len(S) != len(set(S)):
    print("No")
    exit()

flag = True
for s in S:
    if s[0] in first and s[1] in second:
        continue
    else:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
