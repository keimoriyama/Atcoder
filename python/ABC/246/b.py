import math

a, b = map(int, input().split())

x = math.sqrt(a**2 / (a**2 + b**2))
if a == 0:
    y = 1
else:
    y = b * x / a
print(round(x, 7), round(y, 7))