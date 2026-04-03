N = int(input())

s = [0]
for i in range(60):
    if (N >> i) & 1:
        size = len(s)
        for j in range(size):
            num = s[j] | (1 << i)
            s.append(num)

for a in s:
    print(a)
