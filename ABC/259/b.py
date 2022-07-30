import math
a, b, d = map(int, input().split())
th = math.atan2(b, a)
rad = math.radians(d) + th
l = math.sqrt(a * a + b * b)
print(l * math.cos(rad), l * math.sin(rad))