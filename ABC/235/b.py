N = int(input())
H = list(map(int, input().split()))

ans = 0
while ans + 1 < N and H[ans] < H[ans + 1]:
    ans += 1
print(H[ans])
