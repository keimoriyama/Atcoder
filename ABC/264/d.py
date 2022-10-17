from collections import defaultdict

S = input()
m = defaultdict()
m[S] = 0
q = []
q.append(S)

while len(q) > 0:
    current = q.pop(0)
    if current == "atcoder":
        print(m[current])
        exit()
    for i in range(1, 7):
        next = [i for i in current]
        next[i - 1], next[i] = next[i], next[i - 1]
        next = "".join(next)
        if next not in m:
            q.append(next)
            m[next] = m[current] + 1
