from math import sqrt, floor
N = int(input())

b = floor(sqrt(N))
ans = 0
p = []
for i in range(2, b+1):
    while N % i == 0:
        N = N // i
        p.append(i)
if N != 1:
    p.append(N)

for i in range(20):
    if (1 << i) >= len(p):
        ans = i
        break
print(ans)
