N = int(input())
X, Y, Z = [], [], []
for _ in range(N):
    x, y, z = map(int, input().split())
    X.append(x)
    Y.append(y)
    Z.append(z)

seat = 0
majority, diff = [], []
for i, (x, y, z) in enumerate(zip(X, Y, Z)):
    if x > y:
        seat += z
    else:
        majority.append((x + y) // 2 + 1)
        diff.append((x + y) // 2 + 1 - x)
# print(majority)
# print(diff)
a = sorted(zip(diff, majority), reverse=True)
# print(a)
goal = sum(Z) // 2 + 1
# print(goal, seat)
ans = 0
seats = seat
for d, m in a:
    print(d, seats)
    if seats >= goal:
        print(ans)
        exit()
    ans += d
    seats += d
