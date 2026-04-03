from math import floor, ceil

a, b, w = map(int, input().split())

upper = int(floor(1000 * w / a))
lower = int(ceil(1000 * w / b))

if lower > upper:
    print("UNSATISFIABLE")
else:
    print(lower, upper)
