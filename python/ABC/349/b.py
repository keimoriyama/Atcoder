from collections import defaultdict

S = input()
d = defaultdict(int)
for s in S:
    d[s] += 1
c = defaultdict(int)
for v in d.values():
    c[v] += 1

for v in c.values():
    if v != 2:
        print("No")
        exit()

print("Yes")
