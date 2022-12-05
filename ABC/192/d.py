def convert(i, base):
    l = len(i)
    x, idx = 0, 0
    for j in reversed(range(l)):
        n = int(i[idx])
        x += n * base**j
        idx += 1
        if x > M:
            return True
    return False


X = input()
x = [int(i) for i in X]
M = int(input())

d = max(x)
l = d
r = 1000000000000000005

while r - l > 1:
    mid = (l + r) // 2
    if convert(X, mid):
        r = mid
    else:
        l = mid
ans = r - d - 1

if len(x) == 1:
    if int(X) <= M:
        ans = 1
    else:
        ans = 0

print(ans)
