from collections import deque

S = input()

flip = False
T = deque()
for s in S:
    if s == "R":
        flip = not flip
    elif flip:
        if len(T) == 0:
            T.append(s)
        elif T[0] == s:
            T.popleft()
        else:
            T.insert(0, s)
    else:
        if len(T) == 0:
            T.append(s)
        elif T[-1] == s:
            T.pop()
        else:
            T.append(s)

# print(T, flip)
if flip:
    print("".join(list(reversed(T))))
else:
    print("".join(T))
