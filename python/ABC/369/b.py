N = int(input())
pos = [-1, -1]
ans = 0
for _ in range(N):
    a,s =input().split()
    a = int(a)
    hand = (0 if s == 'L' else 1)
    if pos[hand] != -1:
        ans += abs(pos[hand] - a)
    pos[hand] = a
    
print(ans)
