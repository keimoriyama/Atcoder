S = input()
K = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pos = {k: i+1 for i, k in enumerate(S)}
ans = 0
for i in range(1, len(K)):
    prev = pos[K[i-1]]
    current = pos[K[i]]
    ans += abs(prev-current)

print(ans)
