n, k = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())

s = sorted(s[:k])
for a in s:
    print(a)
