N, X = map(int, input().split())
A = list(map(int, input().split()))

total = 0
for i, a in enumerate(A):
    i += 1
    if i % 2 == 0:
        total += a - 1
    else:
        total += a

if total <= X:
    print("Yes")
else:
    print("No")
