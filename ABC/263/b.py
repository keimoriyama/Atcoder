N = int(input())
P = [0, 0] + list(map(int, input().split()))

n = N
ans = 0
while n != 1:
    n = P[n]
    ans += 1

print(ans)
