S = [input() for _ in range(12)]
ans = 0
for i, si in enumerate(S):
    if len(si) == i+1:
        ans += 1
print(ans)
