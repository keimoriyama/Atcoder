A, B = input().split(" ")

sum_A, sum_B = 0, 0

for i in range(len(A)):
    sum_A += int(A[i])
    sum_B += int(B[i])

if sum_A >= sum_B:
    print(sum_A)
else:
    print(sum_B)