N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
L = [i - 1 for i in L]
flag = [False] * (N + 1)
for a in A:
    flag[a] = True

for l in L:
    pos = A[l]
    if pos + 1 == len(flag):
        continue
    if flag[pos + 1]:
        continue
    flag[pos + 1], flag[pos] = True, False
    A[l] = pos + 1


for i, f in enumerate(flag):
    if f:
        print(i, end = " ")
print()
