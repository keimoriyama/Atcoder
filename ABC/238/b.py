N = int(input())
A = list(map(int, input().split()))

for i in range(len(A)):
    A[i] = sum(A[i:])%360
A.append(360)
A.sort()
prev = 0
max_a = 0
for a in A:
    diff = a - prev
    if diff > max_a:
        max_a = diff
    prev = a
print(max_a)
