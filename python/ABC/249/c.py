N, K = map(int, input().split())
S = []
while True:
    try:
        S.append(input())
    except EOFError:
        break
ans = 0
for i in range(2**len(S)):
    check_list = []
    count = {}
    for j in range(len(S)):
        if ((i >> j) & 1):
            check_list.append(S[j])
    #print(check_list)

    for s in check_list:
        for m in s:
            if m not in count.keys():
                count[m] = 1
            else:
                count[m] += 1
    #print(count)
    t = 0
    for num in count.values():
        if num == K:
            t += 1
    if ans < t:
        ans = t
print(ans)