N, Y = map(int, input().split())

man = 10000
gosen = 5000
sen = 1000
flag = False

x, y, z = 0, 0, 0

for x in range(N+1):
    for y in range(N+1):
        z = N - x - y
        if (z >= 0) and (Y == man*x + gosen*y + sen*z):
            flag = True
            break
    if flag == True:
        break

if flag == True:
    print(str(x) + " " + str(y) + " " + str(z))
else:
    print("-1 -1 -1")
