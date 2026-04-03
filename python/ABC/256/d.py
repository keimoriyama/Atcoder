N = int(input())
space = []
for _ in range(N):
    space.append(list(map(int, input().split())))

space = sorted(space, key=lambda x: x[0])

s = [space[0]]
for i in range(1, N):
    e1 = space[i]
    sec = s[-1]
    if sec[1] >= e1[0]:
        if e1[1] > sec[1]:
            sec[1] = e1[1]
        s[-1] = sec
    else:
        s.append(e1)

for i in s:
    print(*i)
