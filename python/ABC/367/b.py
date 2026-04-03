X = input()

out = [False] * len(X)
o = True
for i in reversed(range(len(X))):
    if X[i] == "0" and o:
        out[i] = False
        continue
    out[i] = True
    o = False

for i, o in enumerate(out):
    if X[i] == "." and sum(out[i + 1 :]) == 0:
        break
    if o:
        print(X[i], end="")

print()
