N = int(input())
S = input()

x, y = 0, 0

r = set()
r.add((x, y))

for s in S:
    if s == "R":
        x += 1
    elif s == "L":
        x -= 1
    elif s == "U":
        y += 1
    else:
        y -= 1
    if (x, y) in r:
        print("Yes")
        exit()
    # print(r)
    r.add((x, y))
print("No")
