S = input()

ok = True
for i in range(1, len(S) + 1):
    if 2 <= i and i % 2 == 0 and S[i - 1] == "1":
        ok = False
print("Yes" if ok else "No")
