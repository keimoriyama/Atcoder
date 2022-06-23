N = int(input())
A = input().split()
A = [int(i) for i in A]

mas = [0, 0, 0, 0]
for i in range(len(A)):
    # print(A[i], A[i+1:])
    A[i] += sum(A[i+1:])

# print(A)
p = 0
for a in A:
    if a >= 4:
        p += 1

print(p)
