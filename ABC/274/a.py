from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

A, B = map(int, input().split())
print(Decimal(str(B / A)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))
