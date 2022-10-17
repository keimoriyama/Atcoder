from decimal import ROUND_HALF_UP, Decimal


X, K = map(int, input().split())


for i in range(K + 1):
    e = Decimal("1E" + str(i))
    X = int(Decimal(X).quantize(e, rounding=ROUND_HALF_UP))

print(X)
