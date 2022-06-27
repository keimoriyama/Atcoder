import math
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A = sorted(A)
for _ in range(Q):
    b = int(input())
    left, right = 0, len(A) - 1
    # 2分探索をしたい
    min_value = math.inf
    while left <= right:
        mid = (left + right) // 2
        diff = abs(A[mid] - b)
        min_value = min(min_value, diff)
        if A[mid] < b:
            left = mid + 1
        elif A[mid] > b:
            right = mid - 1
        else:
            break
    print(min_value)
