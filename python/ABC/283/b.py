N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        k = q[1] - 1
        x = q[2]
        A[k] = x
    else:
        k = q[1] - 1
        print(A[k])
