def search(column):
    for i in range(7):
        for j in range(i):
            if column[i] and column[j]:
                for k in range(j + 1, i):
                    if not column[k]:
                        return "Yes"
    return "No"


S = input()

if S[0] == "1":
    print("No")
else:
    c = [False] * 7
    c[0] = S[6] == "1"
    c[1] = S[3] == "1"
    c[2] = (S[1] == "1") and (S[7] == "1")
    c[3] = (S[0] == "1") and (S[4] == "1")
    c[4] = (S[2] == "1") and (S[8] == "1")
    c[5] = S[5] == "1"
    c[6] = S[9] == "1"
    print(search(c))
