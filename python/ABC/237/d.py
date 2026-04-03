from collections import deque

N = int(input())
S = input()

q = deque()
q.append(N)
for i in reversed(range(N)):
    if S[i] == "L":
        q.append(i)
    else:
        q.appendleft(i)

print(*q)
