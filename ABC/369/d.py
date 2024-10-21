N = int(input())
A = list(map(int,input().split()))

dp_odd = [-100] * N
dp_even = [-100] * N
dp_even[0] = 0
dp_odd[0] = A[0]

for i, ai in enumerate(A[1:]):
    i += 1
    dp_even[i] = max(dp_even[i-1], dp_odd[i-1] + 2 * ai)
    dp_odd[i] = max(dp_odd[i-1], dp_even[i-1] + ai)

print(max(dp_even[-1], dp_odd[-1]))
