N, M, H, K = map(int, input().split())
S = input()

I = set()
for _ in range(M):
    x, y = map(int, input().split())
    I.add((x, y))

x, y = 0, 0
for s in S:
    if s == "R":
        x += 1
    elif s == "L":
        x -= 1
    elif s == "U":
        y += 1
    elif s == "D":
        y -= 1
    H -= 1

    if H < 0:
        print("No")
        exit()
    if (x, y) in I and H < K:
        H = K
        I.remove((x, y))

print("Yes")
