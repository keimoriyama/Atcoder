N = int(input())
S = [input() for _ in range(N)]

a, b = 0, 0
for s in S:
    if s == "For":
        a += 1
    else:
        b += 1

if a >= b:
    print("Yes")
else:
    print("No")
