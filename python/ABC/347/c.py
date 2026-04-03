N, A, B = map(int, input().split())
D = [d % (A + B) for d in list(map(int, input().split()))]
D = sorted(list(set(D)))

AB = A + B

ans = False
c = len(D)
for i in range(c):
    D.append(D[i] + AB)
    e = i + c - 1
    if D[e] - D[i] < A:
        ans = True

print("Yes" if ans else "No")
