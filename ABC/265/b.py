N, M, T = map(int, input().split())
A = list(map(int, input().split()))
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))
A.insert(0, 0)
j = 0
for i in range(1, N):
    T -= A[i]
    if j < len(B) and i == B[j][0]:
        T += B[j][1]
        j += 1
    if T <= 0:
        print("No")
        exit()

print("Yes")
