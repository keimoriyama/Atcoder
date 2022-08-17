S = [input()]
S.append(input())

if S[0] == "##" or S[1] == "##":
    print("Yes")
elif S[0][0] == "#" and S[1][0] == "#" or S[0][1] == "#" and S[1][1] == "#":
    print("Yes")
else:
    print("No")
