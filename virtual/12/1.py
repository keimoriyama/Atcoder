N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

flag = [False] * (N + 1)

flag[a] = True
flag[b] = True

for p in P:
    if flag[p]:
        print("NO")
        exit()
    flag[p] = True

print("YES")
