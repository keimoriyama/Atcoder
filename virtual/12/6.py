B = list(map(int, input().split()))
N = int(input())
A = [input() for _ in range(N)]

map_d = {b: i for i, b in enumerate(B)}
