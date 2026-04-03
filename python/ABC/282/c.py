N = int(input())
S = input()

f = [False] * N
flag = True
for i, s in enumerate(S):
    if s == '"':
        flag = not flag
    f[i] = flag

for i in range(N):
    if f[i] and S[i] == ",":
        print(".", end="")
        continue
    print(S[i], end="")
print()
