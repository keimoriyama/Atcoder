N = int(input())
S = input()

l = []
for s in S:
    if len(l) == 0 or l[-1][0] != s:
        l.append([s, 1])
    else:
        l[-1][1] += 1

ret = 0
for i in l:
    ret += i[1]*(i[1]+1)/2
ans = N*(N+1)/2 - ret

print(int(ans))
