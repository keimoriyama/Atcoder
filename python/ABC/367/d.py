N, M = map(int, input().split())
A = list(map(int, input().split()))

i_sum = [[A[i]] for i in range(N)]

# for i in range(N):
#     j = 1
#     while j < N:
#         next = (i + j) % N
#         k = 0
#         while k < next:

print(i_sum)
