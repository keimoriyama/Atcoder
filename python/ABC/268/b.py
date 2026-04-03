S = input()
T = input()

if len(S) > len(T):
    print("No")
    exit()

i = 0
for s in S:
    if T[i] != s:
        print("No")
        exit()
    i += 1
print("Yes")
