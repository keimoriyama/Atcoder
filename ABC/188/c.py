N = int(input())

A_1 = list(input().split(' '))
A = [int(i) for i in A_1]
A_1 = A
tmp,index = [], []
i = 0

# print(A)

while len(A) > 1:
    while i < len(A):
        # print(A[i], A[i+1], max(A[i], A[i+1]))
        """
        if A[i] > A[i+1]:
            tmp.append(A[i])
        else:
            tmp.append(A[i+1])
        """
        tmp.append(max(A[i], A[i+1]))
        i += 2

    if len(A) == 2:
        ans = min(A[0], A[1])
        for j in range(len(A_1)):
            if A_1[j] == ans:
                print(j+1)
    A = tmp
    tmp = []
    i = 0
    # print(A)
    # print(index)

# print(index[-1])