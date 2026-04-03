s = "wbwbwwbwbwbw"
S = s * 100
W, B = map(int, input().split())
for i in range(len(S) - (W + B)):
    s = S[i : i + W + B]
    w, b = 0, 0
    for si in s:
        if si == "w":
            w += 1
        else:
            b += 1
    if w == W and b == B:
        print("Yes")
        exit()

print("No")
