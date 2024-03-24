N, Q = map(int, input().split())
S = input()
A = []
for i in range(N - 1):
    A.append(int(S[i] == S[i + 1]))

B = [0]
for a in A:
    B.append(B[-1] + a)


for _ in range(Q):
    l, r = map(int, input().split())
    print(B[r - 1] - B[l - 1])
