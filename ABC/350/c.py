N = int(input())
A = list(map(int, input().split()))
item2pos = {i + 1: ai for i, ai in enumerate(A)}
pos2item = {ai: i + 1 for i, ai in enumerate(A)}
# print(pos2item)
# print(item2pos)

ans = []
for item1 in range(1, N + 1):
    positem1 = item2pos[item1]
    item2 = pos2item[item1]
    positem2 = item2pos[item2]

    # print(f"item{item1} at {positem1}")
    # print(f"item{item2} at {positem2}")
    if positem1 == positem2:
        continue
    ans.append([item1, item2])
    item2pos[item1] = positem2
    item2pos[item2] = positem1
    pos2item[positem1] = item2
    pos2item[positem2] = item1

print(len(ans))
for ai, aj in ans:
    print(ai, aj)
