N = int(input())
X = []
for i in range(N):
    a, b = map(int, input().split())
    X.append((-a * 10**100 // (a + b), i))

X.sort()
print(*[i + 1 for _, i in X])
