A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))


def S(a, b, c):
    return (
        a[0] * b[1]
        + b[0] * c[1]
        + c[0] * a[1]
        - a[1] * b[0]
        - b[1] * c[0]
        - c[1] * a[0]
    )


if S(A, B, C) > 0 and S(B, C, D) > 0 and S(C, D, A) > 0 and S(D, A, B) > 0:
    print("Yes")
else:
    print("No")
