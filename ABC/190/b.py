N, S, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

f = False
for i in range(N):
    xy = XY[i]
    x = xy[0]
    y = xy[1]
    if x < S and D < y:
        f = True

if f:
    print("Yes")
else:
    print("No")
