N, X = map(int, input().split())

l = []
for i in range(N):
    l.append(list(map(int, input().split())))


ans = 0


def dfs(x, i):
    global ans
    if x == X and i == N:
        ans += 1
        return
    elif i >= N:
        return
    else:
        for item in l[i][1:]:
            dfs(x * item, i + 1)
        return


dfs(1, 0)
print(ans)
