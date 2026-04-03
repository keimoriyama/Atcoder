N = int(input())
a, b = [], []
for _ in range(N):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)

ans = 1000000000
# i番目を固定した時のans
for i, a_i in enumerate(a):
    for j, b_i in enumerate(b):
        if i == j:
            continue
        ans = min(ans, max(a_i, b_i))
for a_i, b_i in zip(a, b):
    ans = min(ans, a_i + b_i)

print(ans)
