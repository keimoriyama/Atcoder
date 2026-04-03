from collections import deque

N = int(input())
A = [-1] + [int(input()) for _ in range(N)]
l = set()
start = 1
i = 0
# print(A)
while start not in l:
    if start == 2:
        print(i)
        exit()
    n = A[start]
    # print(start, n)
    l.add(start)
    start = n
    i += 1

print(-1)
