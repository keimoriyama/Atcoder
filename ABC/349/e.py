def max_white(A, c):
    max_v, max_vi = -1, []
    for i in range(3):
        for j in range(3):
            if c[i][j] != 0:
                continue
            if A[i][j] > max_v:
                max_v = A[i][j]
                max_vi = [i, j]
    return max_v, max_vi


A = [list(map(int, input().split())) for _ in range(3)]
c = [[0, 0, 0] for _ in range(3)]
max_v, max_vi = max_white(A, c)
print(max_v, max_vi)
