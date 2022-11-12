from collections import deque

S = input()
Q = int(input())

d = deque([s for s in S])
reverse = False
for _ in range(Q):
    t = list(input().split())
    t[0] = int(t[0])
    if t[0] == 1:
        # 前後を反転する
        reverse = not (reverse)
    else:
        t[1] = int(t[1])
        if t[1] == 1:
            # 先頭に文字を追加する
            if reverse:
                d.append(t[2])
            else:
                d.appendleft(t[2])
        else:
            # 末尾に文字を追加する
            if reverse:
                d.appendleft(t[2])
            else:
                d.append(t[2])

if not (reverse):
    print("".join(d))
else:
    print("".join(list(reversed(d))))
