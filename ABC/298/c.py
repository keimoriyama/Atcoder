from collections import defaultdict

N = int(input())
Q = int(input())

box = [[] for _ in range(N + 1)]
card = [set() for _ in range(10**6)]
for _ in range(Q):
    i = list(map(int, input().split()))

    if i[0] == 1:
        box[i[2]].append(i[1])
        # box[i[2]] = sorted(box[i[2]])
        card[i[1]].add(i[2])
        # card[i[1]] = sorted(card[i[1]])

    elif i[0] == 2:
        for b in sorted(box[i[1]]):
            print(b, end=" ")
        print()
    else:
        for c in sorted(card[i[1]]):
            print(c, end=" ")
        print()
