from collections import defaultdict

N, Q = map(int, input().split())

yellow = defaultdict(int)
red = defaultdict(int)

for _ in range(Q):
    n, x = map(int, input().split())
    if n == 1:
        yellow[x] += 1
    elif n == 2:
        red[x] += 1
    else:
        if red[x] == 1 or yellow[x] == 2:
            print("Yes")
        else:
            print("No")
