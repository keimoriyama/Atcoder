N, W = map(int, input().split())
A = [int(i) for i in input().split()]

flag = [False for _ in range(W + 1)]
w = 0
for a in A:
    if a <= W:
        flag[a] = True

for i in range(len(A)):
    for j in range(i+1, len(A)):
        w = A[i] + A[j]
        if w <= W:
            flag[w] = True

for i in range(len(A)):
    for j in range(i+1, len(A)):
        for k in range(j+1, len(A)):
            w = A[i]+A[j]+A[k]
            if w <= W:
                flag[w] = True

print(sum(flag))
