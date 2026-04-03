N = int(input())
S = list(map(int, input().split()))

ans = [0]
s_sum = 0
for s in S:
    ans.append(s - s_sum)
    s_sum = sum(ans)

print(*ans[1:])
