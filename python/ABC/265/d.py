from bisect import bisect_left, bisect_right

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

a_rui = [0, A[0]]
for i in range(1, N):
    a_rui.append(a_rui[-1] + A[i])


s = set(a_rui)
for a in range(N):
    y = a_rui[a] + P
    z = a_rui[a] + P + Q
    w = a_rui[a] + P + Q + R
    if y in s and z in s and w in s:
        print("Yes")
        exit()
print("No")
