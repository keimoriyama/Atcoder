N = int(input())
S = input()
x, y = 0, 0
direction = 0
for s in S:
    if s == "S":
        if direction == 0:
            x += 1
        elif direction == 1:
            y -= 1
        elif direction == 2:
            x -= 1
        elif direction == 3:
            y += 1
    elif s == "R":
        direction += 1
        direction %= 4

print(x, y)
