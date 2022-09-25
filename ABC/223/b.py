S = input()
n = len(S)
v = []
for k in range(0, n):
    v.append(S[k:n] + S[0:k])

print(min(v))
print(max(v))
