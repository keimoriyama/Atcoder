S = input()
N = len(S) - 7
if N == 0:
    if S == "keyence":
        print("YES")
        exit()

for i in range(len(S)):
    # print(i)
    # print(S[:i] + S[i + N :])
    if S[:i] + S[i + N :] == "keyence":
        print("YES")
        exit()


print("NO")
