N = int(input())
S = input()
C = list(map(int, input().split()))

# 奇数番目が1、その逆の時のコストを計算するための配列
f0, f1, g0, g1 = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)

for i in range(N):
    f0[i + 1] = f0[i]
    f1[i + 1] = f1[i]
    if i % 2 == 0:
        # 偶数番目が1の配列において、変更する必要があるため、コストを計算する。
        if S[i] == "0":
            f1[i + 1] += C[i]
        # 偶数番目が0の配列において、変更する必要があるため、コストを計算する。
        else:
            f0[i + 1] += C[i]
    else:
        if S[i] == "0":
            f0[i + 1] += C[i]
        else:
            f1[i + 1] += C[i]

for i in reversed(range(N)):
    g0[i] = g0[i + 1]
    g1[i] = g1[i + 1]
    if i % 2 == 0:
        if S[i] == "0":
            g0[i] += C[i]
        else:
            g1[i] += C[i]
    else:
        if S[i] == "0":
            g1[i] += C[i]
        else:
            g0[i] += C[i]

ans = float("inf")
for i in range(1, N):
    ans = min(ans, f0[i] + g0[i], f1[i] + g1[i])

print(ans)
