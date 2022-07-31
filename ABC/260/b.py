N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [i + j for i, j in zip(A, B)]

s = list(zip(range(1, N+1), A, B, C))
s.sort(key = lambda p: (-p[1], p[0]))
s[X:] = sorted(s[X:], key=lambda p: (-p[2], p[0]))
s[X + Y:] = sorted(s[X+Y:], key=lambda p: (-p[3], p[0]))
s[:X + Y + Z] = sorted(s[:X+Y+Z], key=lambda p: p[0])

for p in s[:X + Y + Z]:
    print(p[0])