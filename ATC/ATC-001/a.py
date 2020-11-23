H, W = map(int, input().split())


flag = False
flag2 = [([0] * W) for i in range(H)]


def dfs(maze, x, y, state):
    if x < 0 or y < 0 or x >= W or y >= H:
        return state
    if(maze[x][y] == 'g' and state == True):
        state = True
        return True
    if(flag2[x][y] == 1 or maze[x][y] == '#'):
        return state
    flag2[x][y] = 1
    dfs(maze, x+1, y, state)
    dfs(maze, x, y+1, state)
    dfs(maze, x-1, y, state)
    dfs(maze, x, y-1, state)


b, c = [], []
maze = []
for i in range(H):
    a = input()
    b.append(a)
    for j in range(W):
        c.append(b[i][j])

for k in range(W):
    maze.append(c[k*W:k*W+W])

print(maze)
for i in range(W):
    for j in range(H):
        if maze[i][j] == 's':
            x = i
            y = j
result = dfs(maze, x, y, False)
print(flag)
