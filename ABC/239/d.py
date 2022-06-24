flags = [True] * 201
flags[0], flags[1] = False, False

for i in range(15):
    if not flags[i]:
        continue
    for j in range(i * i, 201, i):
        flags[j] = False

A, B, C, D = map(int, input().split())
for i in range(A, B+1):
    if all(not flags[i + j] for j in range(C, D+1)):
        print("Takahashi")
        exit()
print("Aoki")
