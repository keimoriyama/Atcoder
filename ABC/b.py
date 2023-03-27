N = int(input())
X = sorted(list(map(int, input().split())))
x = []

for i in range(N, 4 * N):
    x.append(X[i])

print(sum(x) / len(x))
