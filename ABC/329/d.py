N, M = map(int, input().split())
A = list(map(int, input().split()))

n = {i: 0 for i in range(1, N + 1)}

max_i = -1
for a in A:
    n[a] += 1
    if max_i == -1:
        max_i = a
    else:
        if n[max_i] == n[a]:
            if max_i > a:
                max_i = a
        elif n[max_i] < n[a]:
            max_i = a
    print(max_i)
    # print(n)
    # n1 = n.copy()
    # n1.sort(key=lambda x: x[1], reverse=True)
    # print(n1[0][0])
