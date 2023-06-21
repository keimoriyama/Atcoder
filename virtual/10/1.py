N = int(input())
H = list(map(int, input().split()))
ans = 0

for i in range(N):
    if H[i] == 0:
        continue
    while H[i] != 0:
        start = i
        end = i
        # 0ではない点で一番後ろにある点を探す
        while H[end] != 0:
            end += 1
            if end == N:
                break
        for j in range(start, end):
            H[j] -= 1
        ans += 1
        # print(H)


print(ans)
