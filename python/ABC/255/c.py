X, A, D, N = map(int, input().split())

if D < 0:
    fi = A + D * (N-1)
    A = fi
    D *= -1

right, left = 0, N

while right <= left:
    mid = (right+left)//2
    if (A + D * mid) <= X:
        right = mid + 1
    else:
        left = mid - 1

i = max(0, right-5)
res = 8e18
while i <= min(N-1, right):
    res = min(abs(A + D * i - X), res)
    i += 1

print(res)
