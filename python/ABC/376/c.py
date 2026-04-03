N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

for i in range(N-1):
    if A[i] > B[i]:
        print(-1)
        exit()

for i in reversed(range(N-1)):
    if A[i+1] > B[i]:
        print(A[i+1])
        exit()

print(A[0])
