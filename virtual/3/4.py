from math import sqrt, radians, sin, cos, atan, pi

N = int(input())
x0, y0 = map(int, input().split())
xN2, yN2 = map(int, input().split())

cx = (x0 + xN2) / 2
cy = (y0 + yN2) / 2

x0 -= cx
y0 -= cy

rad = 2 * pi * 1 / N
x = x0 * cos(rad) - y0 * sin(rad)
y = x0 * sin(rad) + y0 * cos(rad)

print(x + cx, y + cy)
