N = int(input())

A, B = [], []

ans = 0

A = list(input().split(' '))
B = list(input().split(' '))

for i in range(N):
    ans += int(A[i])*int(B[i])

if ans == 0:
    print('Yes')
else:
    print('No')