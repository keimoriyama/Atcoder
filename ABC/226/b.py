N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))
s = set()
for l in L:
    s.add(tuple(l))
print(len(s))
