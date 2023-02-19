N, K = map(int, input().split())
A = sorted(list(set(map(int, input().split()))))

if A[0] != 0:
    print(0)
    exit()
if len(A) == 1 and A[0] == 0:
    print(1)
    exit()

for i in range(min(K - 1, len(A) - 1)):
    if A[i] == A[i + 1] - 1:
        continue
    else:
        print(A[i] + 1)
        exit()
print(K)
