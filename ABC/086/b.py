import math
a, b = input().split()
c = int(a + b)
# print(math.sqrt(c))
d = math.sqrt(c)
if d == math.floor(d):
    print("Yes")
else:
    print("No")
