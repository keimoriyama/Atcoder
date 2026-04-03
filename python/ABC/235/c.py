N, Q = map(int, input().split())
A = list(map(int, input().split()))

a_num = {}

for i in range(len(A)):
    a = A[i]
    if a not in a_num.keys():
        a_num[a] = [i]
    else:
        a_num[a].append(i)


numbers = set(list(a_num.keys()))
for q in range(Q):
    x, k = map(int, input().split())
    if x not in numbers:
        print("-1")
    elif len(a_num[x]) < k:
        print("-1")
    else:
        print(a_num[x][k - 1] + 1)
