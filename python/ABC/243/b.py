N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ans1 = 0
for a, b in zip(A, B):
    if a == b:
        ans1 += 1
print(ans1)
ans2 = 0
for a in A:
    if a in B:
        ans2 += 1
print(ans2 - ans1)
