K = int(input())
A, B = map(list, input().split())
A = reversed([int(i) for i in A])
B = reversed([int(i) for i in B])

n1, n2 = 0, 0
k = 1
for a in A:
    n1 += a * k
    k *= K
k = 1
for b in B:
    n2 += b * k
    k *= K
print(n1 * n2)
