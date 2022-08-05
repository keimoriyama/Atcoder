S = input()
x, y = 0, 0
for s in S:
    if s == "a":
        x += 1
    else:
        break

for s in reversed(S):
    if s == "a":
        y += 1
    else:
        break

if x == len(S):
    print("Yes")
    exit()
elif x > y:
    print("No")
    exit()
else:
    for i in range(x, len(S) - y):
        if S[i] != S[x + len(S) - y - i - 1]:
            print("No")
            exit()
print("Yes")
