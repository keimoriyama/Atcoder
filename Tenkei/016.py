N = int(input())
A, B, C = map(int, input().split())

ans = 100000 
L = 9999
for x in range(L):
    y = 0
    while (A * x + B * y) <= N:
        V = N -  A * x - B * y
        R = x + y + V / C
        if V % C != 0 or V < 0 or R > 9999:
            y += 1
            continue
        z = (N -  A * x - B * y) // C
        ans = min(x + y + z, ans)
        y += 1
print(ans)
