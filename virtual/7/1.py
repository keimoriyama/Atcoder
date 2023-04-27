X, K, D = map(int, input().split())

X = abs(X)

first_step = min(K, X // D)

K -= first_step
X -= first_step * D

if K % 2 == 0:
    print(X)
else:
    print(D - X)
