def print_list(A):
    for a in A:
        if a == 0:
            print()
            break
        print(a, end = " ")

N = int(input())
A = [[0]*(N+1) for i in range(N+1)]
# print(A)
for i in range(1, N+1):
    if i == 1:
        print("1")
    elif i == 2:
        for i in range(2):
            A[2][i] = 1
        print_list(A[2])
    else:
        for j in range(i):
            # print(i,j)
            # print(A[i])
            if j == 0 or j == i:
                A[i][j] = 1
            else:
                A[i][j] = A[i-1][j-1] + A[i-1][j]
        print_list(A[i])
