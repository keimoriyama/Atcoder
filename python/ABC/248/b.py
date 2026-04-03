a, b, k = map(int, input().split())
ans = 0
while b > a:
    a *= k
    ans += 1
    # print(a)
print(ans)