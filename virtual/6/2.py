N = int(input())

left, right = 0, N + 1
m = 0
while right - left > 1:
    m = (left + right) // 2
    sum = m * (m + 1) // 2
    if sum > N + 1:
        right = m
    else:
        left = m

print(N - left + 1)
