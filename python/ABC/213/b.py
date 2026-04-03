N = int(input())
A = list(map(int, input().split()))

d = {v: i + 1 for i, v in enumerate(A)}

A = sorted(A)
print(d[A[-2]])
