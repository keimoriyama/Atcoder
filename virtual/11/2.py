N, M = map(int, input().split())
a = set([int(input()) - 1 for _ in range(M)])

if N == 1:
    print(1)
    exit()

d = [0] * N
if 0 in a and 1 in a:
    pass
elif 0 in a:
    d[1] = 1
elif 1 in a:
    d[0] = 1
else:
    d[0] = 1
    d[1] = 2

for i in range(2, N):
    if i in a:
        continue
    d[i] += d[i - 1] + d[i - 2]
    d[i] %= 1000000007
    # print(d)

print(d[-1])
