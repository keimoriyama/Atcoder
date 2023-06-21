N = int(input())
H = input()

ans = 0
for i in range(1000):
    s = str(i)
    if len(s) < 3:
        s = "0" * (3 - len(s)) + s
    c = 0
    for j in H:
        if j == s[c]:
            c += 1
            if c == 3:
                ans += 1
                break

print(ans)
