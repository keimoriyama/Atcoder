N = int(input())
S = input()
for i in range(1, N):
    c = 0
    for j in range(i, N):
        if S[j] != S[j - i]:
            c += 1
        else:
            break
    print(c)
