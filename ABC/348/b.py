N = int(input())
xy = []

for i in range(N):
    xy.append(list(map(int, input().split())))

for i in range(N):
    xyi = xy[i]
    xi = xyi[0]
    yi = xyi[1]
    max_dist = 0
    max_idx = -1
    ans = -1
    for j in range(N):
        if i == j:
            continue
        xyj = xy[j]
        xj = xyj[0]
        yj = xyj[1]
        dist2 = (xi - xj) ** 2 + (yi - yj) ** 2
        if dist2 > max_dist:
            max_dist = dist2
            max_idx = j

    print(max_idx + 1)
