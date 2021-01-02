N = int(input())

x, y = [], []

for i in range(N):
    tmp = input().split(" ")
    x.append(int(tmp[0]))
    y.append(int(tmp[1].replace("\r", "")))

# print(x)
# print(y)
ans = 0
for i in range(N):
    for j in range(i+1, N):
        grad = (y[i] - y[j])/(x[i] - x[j])
        if abs(grad) <= 1:
            ans += 1

print(ans)