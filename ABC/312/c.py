N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted([i + 1 for i in list(map(int, input().split()))])
event = []
for a in A:
    event.append((a, 0))

for b in B:
    event.append((b, 1))

event.sort()
na, nb = 0, M
for p, t in event:
    if t == 0:
        na += 1
    else:
        nb -= 1
    if na >= nb:
        print(p)
        exit()
