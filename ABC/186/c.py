N = int(input())
ans = 0
for i in range(1, N + 1):
    num_str = str(i)
    if "7" in num_str or "7" in oct(i)[2:]:
        # print(i, oct(i)[2:])
        ans += 1

print(N - ans)
