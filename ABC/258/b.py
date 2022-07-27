N = int(input())
A = []
for _ in range(N):
    A.append(input())
#     
dx = [1, -1, 0]
dy = [1, -1, 0]
ans = 0 
for i in range(N):
    for j in range(N):
        for d_x in dx:
            for d_y in dy:
                if d_x == 0 and d_y == 0:
                    continue
                token = ""
                x, y = i, j
                for _ in range(N):
                    token += A[x][y]
                    x += d_x
                    y += d_y
                    if x < 0:
                        x = N - 1
                    if x > N - 1:
                        x = 0
                    if y < 0:
                        y = N - 1
                    if y > N - 1:
                        y = 0
                ans = max(ans, int(token))
print(ans)
