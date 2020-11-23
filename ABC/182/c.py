N = input()
ans = 1e10

for i in range(len(N)):
    for j in range(i+1, len(N)+1):
        print(N[i:j])
        num = N[i:j]
        if int(num) % 3 == 0:
            tmp = len(N) - len(num)
            if ans > tmp:
                ans = tmp


print(ans)
