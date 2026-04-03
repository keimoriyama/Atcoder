n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

ans = 10000000000000000000000000000000
for m_i in m:
    a = m_i[0]
    p = m_i[1]
    x = m_i[2]
    if a < x:
        ans = min(ans, p)
    else:
        continue

if ans == 10000000000000000000000000000000:
    print(-1)
else:
    print(ans)
