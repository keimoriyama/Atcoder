N = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
# print(a)
ans = 0
for i in range(N):
    # print(a[2 * i + 1])
    ans += a[2 * i + 1]

print(ans)
