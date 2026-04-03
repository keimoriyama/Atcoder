n = [int(i) for i in input().split()]
H = n[0:3]
W = n[3:6]
table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
ans = 0
"""
def dfs(ij):
    i, j = int(ij / 3), int(ij % 3)
    if i == 3:
        ans += 1
        return
    if i == 2:
        x = w[i] - table[0][j] - table[1][j]
        if x <= 0:
            return
        table[i][j] = x
        dfs(ij+1)
    elif j == 2:
        x = h[i] - table[i][0] - table[i][1]
        if x <= 0:
            return
        table[i][j] = x
        dfs(ij+1)
    else:
        for x in range(1, 31):
            table[i][j] = x
            dfs(ij+1)
"""
for a in range(1, 31):
    for b in range(1, 31):
        for d in range(1, 31):
            for e in range(1, 31):
                c = H[0] - a - b
                f = H[1] - d - e
                g = W[0] - a - d
                h = W[1] - b - e
                i = W[2] - c - f
                if min([c,f,g,h,i]) > 0 and g + h + i == H[2]:
                    ans += 1
print(ans)
