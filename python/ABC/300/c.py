H, W = map(int, input().split())

C = [input() for _ in range(H)]

N = min(W, H)
a = [0] * (N + 1)
for j in range(H):
    for k in range(W):
        if C[j][k] == ".":
            continue
        ok = True
        d = 1
        if j - d < 0 or k - d < 0 or j + d >= H or k + d >= W:
            continue
        if (
            C[j - d][k - d] == "#"
            and C[j + d][k - d] == "#"
            and C[j - d][k + d] == "#"
            and C[j + d][k + d] == "#"
        ):
            while True:
                d += 1
                if j - d < 0 or k - d < 0 or j + d >= H or k + d >= W:
                    break
                if not (
                    C[j - d][k - d] == "#"
                    and C[j + d][k - d] == "#"
                    and C[j - d][k + d] == "#"
                    and C[j + d][k + d] == "#"
                ):
                    break

            if ok:
                a[d - 1] += 1


print(*a[1:])
