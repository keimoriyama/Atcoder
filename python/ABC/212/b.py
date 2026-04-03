X = input()
X = [int(x) for x in X]

if X[0] == X[1] == X[2] == X[3]:
    print("Weak")
    exit()

f = 0
for i in range(0, len(X) - 1):
    if X[i] + 1 == X[i + 1] or X[i] == 9 and X[i + 1] == 0:
        f += 1
if f == 3:
    print("Weak")
else:
    print("Strong")
