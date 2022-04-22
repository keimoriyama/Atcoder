import bisect

N = int(input())
A = list(map(int, input().split()))
a_list = [[] for _ in range(N + 1)]
for i, elem in enumerate(A):
    # print(elem, i)
    a_list[elem].append(i + 1)
# print(a_list)
_ = input()
while True:
    try:
        ans = 0
        L, R, X = map(int, input().split())
        a = a_list[X]
        # print(a, L, R, X)
        l = bisect.bisect_left(a, L)
        r = bisect.bisect(a, R)
        # print(l, r)
        print(r - l)
    except EOFError:
        break