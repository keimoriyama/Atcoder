N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A = [-1] + A
added_index = [i for i in range(N + 1)]
inserted = 0
for _ in range(Q):
    l = list(map(int, input().split()))
    if l[0] == 1:
        while added_index:
            i = added_index.pop()
            A[i] = 0
        inserted = l[1]
    if l[0] == 2:
        A[l[1]] += l[2]
        added_index.append(l[1])
    if l[0] == 3:
        print(A[l[1]] + inserted)
