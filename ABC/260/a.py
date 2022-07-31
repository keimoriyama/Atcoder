S = input()
d = {}
for s in S:
    if s not in d.keys():
        d[s] = 1
    else: 
        d[s] += 1

for k, v in zip(d.keys(), d.values()):
    if v == 1:
        print(k)
        break
    elif v == 3:
        print(-1)
        break