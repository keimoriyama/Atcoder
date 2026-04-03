from math import factorial

P = int(input())

ans = 0
for i in range(10, 0, -1):
    while factorial(i) <= P:
        P -= factorial(i)
        ans += 1

print(ans)
