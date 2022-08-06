X, Y = map(int, input().split())

ans = (Y - X) // 10
mod = (Y - X) % 10
if mod != 0:
    ans += 1

if ans < 0:
    print(0)
else:
    print(ans)
