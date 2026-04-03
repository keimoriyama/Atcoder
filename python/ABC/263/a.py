A = sorted(list(map(int, input().split())))

d = {}
for a in A:
    if a in d.keys():
        d[a] += 1
    else:
        d[a] = 1

if 3 in d.values() and 2 in d.values():
    print("Yes")
else:
    print("No")
