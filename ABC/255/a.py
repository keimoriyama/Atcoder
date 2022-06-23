R, C = map(int, input().split())
R -= 1
C -= 1
A = input().split()
B = input().split()

if R == 0:
    print(A[C])
else:
    print(B[C])
