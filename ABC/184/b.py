N, X = map(int, input().split())
S = input()

for ans in S:
    if ans == 'o':
        X += 1

    elif ans == 'x':
        if X > 0:
            X -= 1

print(X)
