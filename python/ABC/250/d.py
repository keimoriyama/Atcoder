def gen_num(N):
    num = []
    flag = [False] * (N+1)
    flag[0] = True
    flag[1] = True
    for i in range(2, N+1):
        if flag[i]:
            continue
        num.append(i)
        for j in range(i*i, N+1, i):
            flag[j] = True
    return num

ans = 0
N = int(input())
S = gen_num(10**6)
for i, q in enumerate(S):
    t = q ** 3
    for j in range(i):
        if t * S[j] > N:
            break
        ans += 1
print(ans)
