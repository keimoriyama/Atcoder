import itertools

N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [tuple(map(int, input().split())) for _ in range(K)]

ans = 0
for balls in itertools.product(*CD):
    balls = set(balls)
    c = sum(A in balls and B in balls for A, B in AB)
    if ans < c:
        ans = c

print(ans)
