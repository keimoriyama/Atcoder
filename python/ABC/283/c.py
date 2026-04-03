S = input()

ans = 0
z_count = 0
z_dcount = 0
i = 0
while i < len(S):
    s = S[i]
    if s != "0":
        ans += 1
        i += 1
    if s == "0":
        if len(S[i + 1 :]) > 0:
            if S[i + 1] == "0":
                z_dcount += 1
                i += 2
            else:
                z_count += 1
                i += 1
        else:
            z_count += 1
            i += 1


print(ans + z_count + z_dcount)
