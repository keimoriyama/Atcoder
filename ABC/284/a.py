N = int(input())

S = [input() for _ in range(N)]

for i in reversed(range(N)):
    print(S[i])
