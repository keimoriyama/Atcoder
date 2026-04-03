N = int(input())
H = list(map(int, input().split()))

max = -1
max_i = 0
for i in range(N):
    if H[i] > max:
        max = H[i]
        max_i = i + 1

print(max_i)
