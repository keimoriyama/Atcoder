N = int(input())
A = list(map(int, input().split()))

called = set()
for i, a in enumerate(A):
    i += 1
    if i in called:
        continue
    called.add(a)
ans = []

for i in range(1, N + 1):
    if i in called:
        continue
    ans.append(i)

print(len(ans))
print(*ans)
